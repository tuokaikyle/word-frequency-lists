-- produce lexique4_top_5000.tsv
SELECT "1_Mot", "4_Lemme", "5_Cgram", "7_Genre", "10_FreqMot" 
FROM public.lexique4
order by "10_FreqMot" desc 
limit 5000

-- count distinct lemmes: 2921
WITH top_words AS (
    SELECT "1_Mot", "4_Lemme", "5_Cgram", "7_Genre", "10_FreqMot"
    FROM public.lexique4
    ORDER BY "10_FreqMot" DESC
    LIMIT 5000
)
SELECT COUNT(DISTINCT "4_Lemme") AS distinct_lemmes
FROM top_words;

-- explore the data
select * from public.lexique4 l where l."1_Mot" = 'maisons'

select * from public.lexique4 l where l."4_Lemme" = 'accord'

SELECT *
FROM public.lexique4
order by "10_FreqMot" desc 
limit 5000