# ==============================================================================
# Script: run-simulator.ps1
# Descricao: Roda o simulador de operacao (shared/gen/simulator, ADR 009) a
#            partir da raiz do repo, com o venv de shared/gen e log em
#            logs/simulator.log (UTF-8).
#
# Por padrao roda SO O HISTORICO: para no instante em que o script foi chamado
# (ADR 013: o historico roda sem conectores; o tempo real so depois do passo 5
# da F5.3). Use -Live para seguir em tempo real depois do historico.
#
# Retomada: o relogio volta ao ultimo evento gravado no banco, entao rodar de
# novo continua de onde parou. -Days so vale na primeira execucao (banco sem
# pedidos) e o restock inicial do seed precisa ser anterior ou igual ao inicio.
# Ctrl-C para limpo: cada acao e uma transacao.
#
# Codigo de saida: o mesmo do simulador (0 ok, 2 se recusou comecar, outro = erro).
#
# Uso:
#   .\scripts\simulator\run-simulator.ps1 -Days 365 -Seed 42   # historico de 1 ano
#   .\scripts\simulator\run-simulator.ps1 -Live                # historico + tempo real
#   .\scripts\simulator\run-simulator.ps1 -Status              # contagens, sem rodar
# ==============================================================================

param(
    [int]$Days,
    [int]$Seed,
    [switch]$Live,
    [switch]$Status
)

$ErrorActionPreference = "Stop"

$repoRoot = (git rev-parse --show-toplevel 2>$null)
if (-not $repoRoot) { $repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot) }
$genDir = Join-Path $repoRoot "shared\gen"
$python = Join-Path $genDir ".venv\Scripts\python.exe"
$envFile = Join-Path $genDir ".env"

if (-not (Test-Path $envFile)) {
    Write-Host "[ERRO] shared\gen\.env nao encontrado." -ForegroundColor Red
    exit 1
}
$envText = Get-Content $envFile -Raw

if ($Status) {
    # Contagens por tabela no Postgres, sem imprimir registro de pessoa e sem exigir os sais.
    $pgUser = ([regex]::Match($envText, "(?m)^POSTGRES_USERNAME=([^\r\n]+)").Groups[1].Value).Trim()
    $pgDb = ([regex]::Match($envText, "(?m)^POSTGRES_DB=([^\r\n]+)").Groups[1].Value).Trim()
    $sql = "select 'orders=' || count(*) from ubereats.orders union all " +
        "select 'payments=' || count(*) from ubereats.payments union all " +
        "select 'deliveries=' || count(*) from ubereats.deliveries union all " +
        "select 'ultimo_pedido=' || coalesce(max(placed_at)::text, '-') from ubereats.orders"
    docker exec postgres-ubereats psql -U $pgUser -d $pgDb -Atc $sql
    exit $LASTEXITCODE
}

if (-not (Test-Path $python)) {
    Write-Host "[ERRO] venv nao encontrado em shared\gen\.venv. Crie com: python -m venv shared\gen\.venv ; shared\gen\.venv\Scripts\pip install -r shared\gen\requirements.txt" -ForegroundColor Red
    exit 1
}
foreach ($key in @("TRACKING_SALT_ORDER", "TRACKING_SALT_PAYMENT")) {
    # [^\r\n]+ e nao ".+": com CRLF o ponto casaria o "\r" e uma linha vazia passaria.
    if ($envText -notmatch "(?m)^$key=[^\r\n]+") {
        Write-Host "[ERRO] $key ausente ou vazio no shared\gen\.env." -ForegroundColor Red
        exit 1
    }
}

$logDir = Join-Path $repoRoot "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "simulator.log"

$cliArgs = @("-m", "simulator", "run")
if ($PSBoundParameters.ContainsKey("Days")) { $cliArgs += @("--days", $Days) }
if ($PSBoundParameters.ContainsKey("Seed")) { $cliArgs += @("--seed", $Seed) }
if (-not $Live) {
    # Historico apenas: para agora (hora local da maquina, que e o fuso do simulador).
    $cliArgs += @("--until", (Get-Date).ToString("yyyy-MM-ddTHH:mm:ss"))
}

Write-Host "[INFO] simulador: python $($cliArgs -join ' ')  (log: $logFile)"
Push-Location $genDir
$oldEncoding = [Console]::OutputEncoding
$oldEap = $ErrorActionPreference
try {
    # UTF-8 ponta a ponta (sem isso os acentos saem quebrados no console e no log).
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    $env:PYTHONIOENCODING = "utf-8"
    $env:PYTHONUNBUFFERED = "1"
    # O logging do Python escreve em stderr; no Windows PowerShell 5.1 isso viraria erro
    # terminante com "Stop". Com "Continue" o texto passa e o codigo de saida segue valendo.
    $ErrorActionPreference = "Continue"
    & $python @cliArgs 2>&1 | ForEach-Object {
        $line = "$_"
        $line
        Add-Content -Path $logFile -Value $line -Encoding utf8
    }
    $code = $LASTEXITCODE
}
finally {
    $ErrorActionPreference = $oldEap
    [Console]::OutputEncoding = $oldEncoding
    Remove-Item Env:\PYTHONIOENCODING -ErrorAction SilentlyContinue
    Remove-Item Env:\PYTHONUNBUFFERED -ErrorAction SilentlyContinue
    Pop-Location
}
exit $code
