#Quan sát view khi có một đăng ký mới
#bước 1
BEGIN;

#bước 2
INSERT INTO enrollments (student_id, class_section_id)
VALUES ('22000004', 'WEB-01');

#Xem kết quả rồi hoàn tác
#bước 3
SELECT class_id, capacity, enrolled, remaining
FROM v_section_summary
WHERE class_id = 'WEB-01';

#bước 4
ROLLBACK;

#bước 5
SELECT class_id, capacity, enrolled, remaining
FROM v_section_summary
WHERE class_id = 'WEB-01';

