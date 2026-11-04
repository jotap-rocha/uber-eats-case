// Inicia o replica set rs0 (F4.4 do modelo físico; ADR 011) antes de criar a coleção.
// O entrypoint da imagem mongo:7 só tira o --replSet do mongod temporário do init quando há usuário
// root (autenticação); sem autenticação, o init roda em replica set ainda não iniciado e nenhuma
// escrita passa ("not primary"). Conferido no docker-entrypoint.sh da imagem, 2026-11-04.
// O membro é localhost:27017 porque o mongod do init só escuta em 127.0.0.1. Clientes fora do
// compose usam directConnection=true (F4.4); a partir do Windows, localhost:27017 é a porta publicada.
try {
  rs.status();
} catch (e) {
  rs.initiate({ _id: "rs0", members: [{ _id: 0, host: "localhost:27017" }] });
}

let tentativas = 0;
while (!db.hello().isWritablePrimary) {
  if (++tentativas > 60) {
    throw new Error("replica set rs0 sem primário depois de 60 s");
  }
  sleep(1000);
}
print("ok: replica set rs0 primário");
