-- upgrade --
ALTER TABLE "user" ADD "username" VARCHAR(40) NOT NULL;
-- downgrade --
ALTER TABLE "user" DROP COLUMN "username";
