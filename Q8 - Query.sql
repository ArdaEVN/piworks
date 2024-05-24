WITH country_medians AS (
    SELECT 
        country, 
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY daily_vaccinations) AS median_vaccinations
    FROM 
        country_vaccination_stats
    WHERE 
        daily_vaccinations IS NOT NULL
    GROUP BY 
        country
),
imputed_values AS (
    SELECT 
        cvs.country, 
        cvs.date, 
        COALESCE(cvs.daily_vaccinations, cm.median_vaccinations, 0) AS daily_vaccinations
    FROM 
        country_vaccination_stats cvs
    LEFT JOIN 
        country_medians cm
    ON 
        cvs.country = cm.country
)

UPDATE country_vaccination_stats
SET daily_vaccinations = iv.daily_vaccinations
FROM imputed_values iv
WHERE country_vaccination_stats.country = iv.country
AND country_vaccination_stats.date = iv.date
AND country_vaccination_stats.daily_vaccinations IS NULL;
