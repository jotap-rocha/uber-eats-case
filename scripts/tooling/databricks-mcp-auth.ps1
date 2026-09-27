$hostUrl = "https://dbc-029603a1-3b9b.cloud.databricks.com"

$clientId = $env:DATABRICKS_SP_CLIENT_ID.Trim()
$clientSecret = $env:DATABRICKS_SP_CLIENT_SECRET.Trim()

$encodedId = [Uri]::EscapeDataString($clientId)
$encodedSecret = [Uri]::EscapeDataString($clientSecret)
$pair = "$($encodedId):$($encodedSecret)"
$basicAuth = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes($pair))

try {
    $response = Invoke-RestMethod -Uri "$hostUrl/oidc/v1/token" `
        -Method Post `
        -Headers @{ Authorization = "Basic $basicAuth" } `
        -Body @{ grant_type = "client_credentials"; scope = "all-apis" } `
        -ContentType "application/x-www-form-urlencoded"
}
catch {
    Write-Error "Falha ao obter token: $($_.Exception.Message)"
    exit 1
}

@{ Authorization = "Bearer $($response.access_token)" } | ConvertTo-Json -Compress