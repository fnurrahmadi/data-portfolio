-- check duplicates
select title, count(1)
from games g 
group by 1
having count(1) > 1
;

-- check nulls
select
sum(case when title is null or title = '' then 1 end) as title_null,
sum(case when original_price is null or original_price = '' then 1 end) as original_price_null,
sum(case when discounted_price is null or discounted_price = '' then 1 end) as discounted_price_null,
sum(case when release_date is null or release_date = '' then 1 end) as release_date_null,
sum(case when link is null or link = '' then 1 end) as link_null,
sum(case when game_description is null or game_description = '' then 1 end) as game_description_null,
sum(case when recent_reviews_summary is null or recent_reviews_summary = '' then 1 end) as recent_reviews_summary_null,
sum(case when all_reviews_summary is null or all_reviews_summary = '' then 1 end) as all_reviews_summary_null,
sum(case when recent_reviews_number is null or recent_reviews_number = '' then 1 end) as recent_reviews_number_null,
sum(case when all_reviews_number is null or all_reviews_number = '' then 1 end) as all_reviews_number_null,
sum(case when developer is null or developer = '' then 1 end) as developer_null,
sum(case when publisher is null or publisher = '' then 1 end) as publisher,
sum(case when supported_languages is null or supported_languages = '' then 1 end) as supported_languages_null,
sum(case when popular_tags is null or popular_tags = '' then 1 end) as popular_tags_null,
sum(case when game_features is null or game_features = '' then 1 end) as game_features_null,
sum(case when minimum_requirements is null or minimum_requirements = '' then 1 end) as minimum_requirements_null
from games g 
;

-- check unique values
-- title
select title, count(1)
from games g
group by 1
order by 1 asc
;
-- original price
select original_price, count(1)
from games g
group by 1
order by 1 asc
;
-- discounted price
select discounted_price, count(1)
from games g
group by 1
order by 1 asc
;
-- release date
select release_date, count(1)
from games g
group by 1
--order by 1 asc
;
-- link
select link, count(1)
from games g
group by 1
order by 1 asc
;
-- game description
select game_description, count(1)
from games g
group by 1
order by 1 asc
;
-- recent reviews summary
select recent_reviews_summary, count(1)
from games g
group by 1
order by 1 asc
;
-- all reviews summary
select all_reviews_summary, count(1)
from games g
group by 1
order by 1 asc
;
-- recent_reviews_number
select recent_reviews_number, count(1)
from games g
group by 1
order by 1 asc
;
-- all reviews number
select all_reviews_number, count(1)
from games g
group by 1
order by 1 asc
;
-- developer
select developer, count(1)
from games g
group by 1
order by 1 asc
;
-- publisher
select publisher, count(1)
from games g
group by 1
order by 1 asc
;
-- supported languages
select supported_languages, count(1)
from games g
group by 1
order by 1 asc
;
-- popular tags
select popular_tags, count(1)
from games g
group by 1
order by 1 asc
;
-- game features
select game_features, count(1)
from games g
group by 1
order by 1 asc
;
-- minimum requirements
select minimum_requirements, count(1)
from games g
group by 1
order by 1 asc
;

-- fixing columns
select 
case when title = '' then null else title end as title
,(case when lower(original_price) like 'free' then '0' else replace(trim(leading '$' from original_price),',','') end)::numeric as original_price
,(case when lower(discounted_price) like 'free' then '0' else replace(trim(leading '$' from discounted_price),',','') end)::numeric as discounted_price
,(case when substr(release_date, 1, 1) between '0' and '9' and release_date like '%,%' then release_date end)::date as date
,link
,case when game_description = '' then null else game_description end as game_description
,case when recent_reviews_summary is null or recent_reviews_summary = '' or recent_reviews_summary like '%user reviews%' then 'Not Enough Reviews' end as recent_reviews_summary
,case when all_reviews_summary is null or all_reviews_summary = '' then 'Not Enough Reviews' end as all_reviews_summary
,case when recent_reviews_number is null or recent_reviews_number = '' then null else trim(substring(recent_reviews_number from '- (.*?)(?=%)'))::numeric * 0.01 end as recent_reviews_number_positive
,case when all_reviews_number is null or all_reviews_number = '' then null else trim(substring(all_reviews_number from '- (.*?)(?=%)'))::numeric * 0.01 end as all_reviews_number_positive
,case when recent_reviews_number is null or recent_reviews_number = '' then null else replace(trim(substring(recent_reviews_number from '(?<=of the\s)(.*?)(?=\suser\sreviews)')),',','')::numeric end as recent_reviews_number_total
,case when all_reviews_number is null or all_reviews_number = '' then null else replace(trim(substring(all_reviews_number from '(?<=of the\s)(.*?)(?=\suser\sreviews)')),',','')::numeric end as all_reviews_number_total
,case when developer = '' then null else developer end as developer
,case when publisher = '' then null else publisher end as publisher
,case when lower(supported_languages) like '%english%' then 1 else 0 end as supported_language_eng
,case when lower(supported_languages) like '%german%' then 1 else 0 end as supported_language_ger
,case when lower(supported_languages) like '%french%' then 1 else 0 end as supported_language_fre
,case when lower(supported_languages) like '%italian%' then 1 else 0 end as supported_language_ita
,case when lower(supported_languages) like '%russian%' then 1 else 0 end as supported_language_rus
,case when lower(supported_languages) like '%spanish%' then 1 else 0 end as supported_language_spa
,case when lower(supported_languages) like '%portuguese%' then 1 else 0 end as supported_language_por
,case when lower(supported_languages) like '%chinese%' then 1 else 0 end as supported_language_chi
,case when lower(supported_languages) like '%japanese%' then 1 else 0 end as supported_language_jap
,case when lower(popular_tags) like '%action%' then 1 else 0 end as popular_tag_act
,case when lower(popular_tags) like '%adventure%' then 1 else 0 end as popular_tag_adv
,case when lower(popular_tags) like '%multiplayer%' then 1 else 0 end as popular_tag_mul
,case when lower(popular_tags) like '%singleplayer%' then 1 else 0 end as popular_tag_sin
,case when lower(popular_tags) like '%horror%' then 1 else 0 end as popular_tag_hor
,case when lower(popular_tags) like '%indie%' then 1 else 0 end as popular_tag_ind
,case when lower(popular_tags) like '%rpg%' then 1 else 0 end as popular_tag_rpg
,case when lower(popular_tags) like '%strategy%' then 1 else 0 end as popular_tag_str
,case when lower(popular_tags) like '%platform%' then 1 else 0 end as popular_tag_pla
,case when lower(popular_tags) like '%shoot%' then 1 else 0 end as popular_tag_sho
,case when lower(game_features) like '%cross-platform%' then 1 else 0 end as game_feature_cross
,case when lower(game_features) like '%steam cloud%' then 1 else 0 end as game_feature_cloud
,case when lower(game_features) like '%in-app purchases%' then 1 else 0 end as game_feature_inapp
,case when lower(game_features) like '%trading cards%' then 1 else 0 end as game_feature_cards
,case when lower(game_features) like '%vr supported%' then 1 else 0 end as game_feature_vr
,case when lower(game_features) like '%anti-cheat%' then 1 else 0 end as game_feature_ac
,case when game_features like '%LAN%' then 1 else 0 end as game_feature_lan
,case when game_features like '%MMO%' then 1 else 0 end as game_feature_mmo
,case when minimum_requirements = '' then null else minimum_requirements end as minimum_requirements
from games g
;

-- create a new table with the cleaned data
drop table if exists games_cleaned;
create table if not exists games_cleaned
as
select 
case when title = '' then null else title end as title
,(case when lower(original_price) like 'free' then '0' else replace(trim(leading '$' from original_price),',','') end)::numeric as original_price
,(case when lower(discounted_price) like 'free' then '0' else replace(trim(leading '$' from discounted_price),',','') end)::numeric as discounted_price
,(case when substr(release_date, 1, 1) between '0' and '9' and release_date like '%,%' then release_date end)::date as date
,link
,case when game_description = '' then null else game_description end as game_description
,case when recent_reviews_summary is null or recent_reviews_summary = '' or recent_reviews_summary like '%user reviews%' then 'Not Enough Reviews' end as recent_reviews_summary
,case when all_reviews_summary is null or all_reviews_summary = '' then 'Not Enough Reviews' end as all_reviews_summary
,case when recent_reviews_number is null or recent_reviews_number = '' then null else trim(substring(recent_reviews_number from '- (.*?)(?=%)'))::numeric * 0.01 end as recent_reviews_number_positive
,case when all_reviews_number is null or all_reviews_number = '' then null else trim(substring(all_reviews_number from '- (.*?)(?=%)'))::numeric * 0.01 end as all_reviews_number_positive
,case when recent_reviews_number is null or recent_reviews_number = '' then null else replace(trim(substring(recent_reviews_number from '(?<=of the\s)(.*?)(?=\suser\sreviews)')),',','')::numeric end as recent_reviews_number_total
,case when all_reviews_number is null or all_reviews_number = '' then null else replace(trim(substring(all_reviews_number from '(?<=of the\s)(.*?)(?=\suser\sreviews)')),',','')::numeric end as all_reviews_number_total
,case when developer = '' then null else developer end as developer
,case when publisher = '' then null else publisher end as publisher
,case when lower(supported_languages) like '%english%' then 1 else 0 end as supported_language_eng
,case when lower(supported_languages) like '%german%' then 1 else 0 end as supported_language_ger
,case when lower(supported_languages) like '%french%' then 1 else 0 end as supported_language_fre
,case when lower(supported_languages) like '%italian%' then 1 else 0 end as supported_language_ita
,case when lower(supported_languages) like '%russian%' then 1 else 0 end as supported_language_rus
,case when lower(supported_languages) like '%spanish%' then 1 else 0 end as supported_language_spa
,case when lower(supported_languages) like '%portuguese%' then 1 else 0 end as supported_language_por
,case when lower(supported_languages) like '%chinese%' then 1 else 0 end as supported_language_chi
,case when lower(supported_languages) like '%japanese%' then 1 else 0 end as supported_language_jap
,case when lower(popular_tags) like '%action%' then 1 else 0 end as popular_tag_act
,case when lower(popular_tags) like '%adventure%' then 1 else 0 end as popular_tag_adv
,case when lower(popular_tags) like '%multiplayer%' then 1 else 0 end as popular_tag_mul
,case when lower(popular_tags) like '%singleplayer%' then 1 else 0 end as popular_tag_sin
,case when lower(popular_tags) like '%horror%' then 1 else 0 end as popular_tag_hor
,case when lower(popular_tags) like '%indie%' then 1 else 0 end as popular_tag_ind
,case when lower(popular_tags) like '%rpg%' then 1 else 0 end as popular_tag_rpg
,case when lower(popular_tags) like '%strategy%' then 1 else 0 end as popular_tag_str
,case when lower(popular_tags) like '%platform%' then 1 else 0 end as popular_tag_pla
,case when lower(popular_tags) like '%shoot%' then 1 else 0 end as popular_tag_sho
,case when lower(game_features) like '%cross-platform%' then 1 else 0 end as game_feature_cross
,case when lower(game_features) like '%steam cloud%' then 1 else 0 end as game_feature_cloud
,case when lower(game_features) like '%in-app purchases%' then 1 else 0 end as game_feature_inapp
,case when lower(game_features) like '%trading cards%' then 1 else 0 end as game_feature_cards
,case when lower(game_features) like '%vr supported%' then 1 else 0 end as game_feature_vr
,case when lower(game_features) like '%anti-cheat%' then 1 else 0 end as game_feature_ac
,case when game_features like '%LAN%' then 1 else 0 end as game_feature_lan
,case when game_features like '%MMO%' then 1 else 0 end as game_feature_mmo
,case when minimum_requirements = '' then null else minimum_requirements end as minimum_requirements
from games g
;

-- check new cleaned table
select *
from games_cleaned 
--limit 50
;