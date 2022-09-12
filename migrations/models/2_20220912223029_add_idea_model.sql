-- upgrade --
CREATE TABLE IF NOT EXISTS "idea" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "content" TEXT NOT NULL,
    "visibility" VARCHAR(9) NOT NULL  DEFAULT 'PUBLIC',
    "author_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "idea"."visibility" IS 'PUBLIC: PUBLIC\nPROTECTED: PRIVATE\nPRIVATE: PROTECTED';
COMMENT ON TABLE "idea" IS 'Idea model ';;
CREATE TABLE IF NOT EXISTS "user" (
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "first_name" VARCHAR(30) NOT NULL,
    "hash" VARCHAR(128) NOT NULL,
    "id" UUID NOT NULL  PRIMARY KEY,
    "last_name" VARCHAR(30) NOT NULL,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "username" VARCHAR(40) NOT NULL
);
COMMENT ON TABLE "user" IS 'User model ';-- downgrade --
DROP TABLE IF EXISTS "idea";
DROP TABLE IF EXISTS "user";
