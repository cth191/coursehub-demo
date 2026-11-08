BEGIN;

-- 1. Bo sung cot note vao bang enrollment_events
ALTER TABLE enrollment_events
ADD COLUMN note VARCHAR(200);

-- 2. Ghi nhan migration da duoc ap dung
INSERT INTO schema_migrations (version, description)
VALUES (
    '002',
    'Add note column to enrollment_events'
);

COMMIT;
