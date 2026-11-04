// Coleção restaurant_profiles com validador $jsonSchema e índice único (F3.2 do modelo físico).
// Gerado a partir de shared/docs/modelagem/04-modelo-fisico.md. Roda uma vez, no init do volume
// (o entrypoint roda sem --replSet; o replica set nasce no healthcheck, F4.4). Os perfis são
// gravados pelo seed em Python (F3, decisão 1), não aqui.
// Banco ubereats, coleção restaurant_profiles (um documento por restaurante).
db = db.getSiblingDB("ubereats");

const hhmm = "^([01][0-9]|2[0-3]):[0-5][0-9]$";

db.createCollection("restaurant_profiles", {
  validationLevel: "strict",
  validationAction: "error",
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["_id", "service_windows", "menu_items", "created_at", "updated_at"],
      additionalProperties: false,
      properties: {
        _id: { bsonType: "long", minimum: 1, description: "restaurant_id (ext → Postgres.restaurants)" },
        service_windows: {
          bsonType: "array", minItems: 1, maxItems: 2,
          items: {
            bsonType: "object",
            required: ["start_time", "end_time"],
            additionalProperties: false,
            properties: {
              start_time: { bsonType: "string", pattern: hhmm },
              end_time: { bsonType: "string", pattern: hhmm }
            }
          }
        },
        menu_items: {
          bsonType: "array", minItems: 1,
          items: {
            bsonType: "object",
            required: ["product_id", "section", "display_order", "highlighted", "customizations"],
            additionalProperties: false,
            properties: {
              product_id: { bsonType: "long", minimum: 1 },
              section: { enum: ["starters", "mains", "sides", "desserts", "drinks", "combos"] },
              display_order: { bsonType: "int", minimum: 1 },
              highlighted: { bsonType: "bool" },
              customizations: {
                bsonType: "array", uniqueItems: true,
                items: { bsonType: "string", minLength: 1, maxLength: 60 }
              }
            }
          }
        },
        created_at: { bsonType: "date" },
        updated_at: { bsonType: "date" }
      }
    }
  }
});

// Um produto aparece no máximo uma vez em todo o conjunto de cardápios (cada produto é de um só restaurante).
db.restaurant_profiles.createIndex({ "menu_items.product_id": 1 }, { name: "uq_restaurant_profiles_product", unique: true });
print("ok: coleção e índice criados");
