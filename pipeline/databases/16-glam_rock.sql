-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

-- Requirements:

-- Import this table dump: metal_bands.sql.zip
-- Column names must be:
-- band_name
-- lifespan until 2020 (in years)
-- You should use attributes formed and split for computing the lifespan
-- Your script can be executed on any database

-- SELECT band_name, IFNULL(split, 2020) - IFNULL(formed, 0) AS lifespan


-- USE metal_bands;
-- SELECT band_name, IF(split IS NULL, 2020, split) - IF(formed IS NULL,0,formed) AS lifespan FROM me
--tal_bands ORDER BY lifespan DESC;


-- Create a view to compute the lifespan of each band
CREATE OR REPLACE VIEW band_lifespan AS
SELECT
    band_name,
    IFNULL(split, YEAR('2020-01-01')) - formed AS lifespan
FROM
    metal_bands;

-- List all bands with Glam rock as their main style, ranked by their longevity
SELECT
    band_name,
    lifespan
FROM
    band_lifespan
WHERE
    band_name IN ('Alice Cooper', 'Mötley Crüe', 'Marilyn Manson', 'The 69 Eyes', 'Hardcore Superstar', 'Nasty Idols', 'Hanoi Rocks')
ORDER BY
    lifespan DESC;

