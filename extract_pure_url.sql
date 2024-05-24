-- Example table
CREATE TABLE device_stats (
    Device_Type VARCHAR(20),
    Stats_Access_Link TEXT
);

-- Insert example data
INSERT INTO device_stats (Device_Type, Stats_Access_Link)
VALUES
('AXO145', '<url>https://xcd32112.smart_meter.com</url>'),
('TRU151', '<url>http://txh67.dia_meter.com</url>'),
('ZOD231', '<url>http://yt5495.smart_meter.com</url>'),
('YRT326', '<url>https://ret323_TRu.crown.com</url>'),
('LWR245', '<url>https://luwr3243.celcius.com</url>');

-- Query to extract pure URL
SELECT 
    Device_Type,
    REGEXP_REPLACE(
        REGEXP_REPLACE(Stats_Access_Link, '<url>https?://', '', 'g'),
        '</url>', '', 'g'
    ) AS Pure_URL
FROM 
    device_stats;
