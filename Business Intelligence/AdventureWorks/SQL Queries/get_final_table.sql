--create table master_table
--as
select
	sfis."OrderDate" ,
	extract(YEAR from sfis."OrderDate") as OrderYear ,
	extract(MONTH from sfis."OrderDate") as OrderMonth ,
	extract(DAY from sfis."OrderDate") as OrderDay ,
	extract(ISODOW from sfis."OrderDate") as OrderDOW ,
	sdst."SalesTerritoryRegion", sdst."SalesTerritoryCountry", sdst."SalesTerritoryGroup",
	sdpc1."EnglishProductName", sdpc1."EnglishProductSubcategoryName", sdpc1."EnglishProductCategoryName",
	sdsr1."SalesReasonName", sdsr1."SalesReasonReasonType" ,
	sfis."SalesAmount", sfis."TotalProductCost", sfis."SalesAmount" - sfis."TotalProductCost" as NettProfit
from "stg_FactInternetSales" sfis
left join (
	select "SalesOrderNumber", sdsr."SalesReasonName", sdsr."SalesReasonReasonType" 
	from "stg_FactInternetSalesReason" sfisr
	left join "stg_DimSalesReason" sdsr 
		on sfisr."SalesReasonKey" = sdsr."SalesReasonKey") sdsr1
	on sfis."SalesOrderNumber" = sdsr1."SalesOrderNumber"
left join "stg_DimSalesTerritory" sdst
	on sfis."SalesTerritoryKey" = sdst."SalesTerritoryKey"
left join (
	select sdp."ProductKey", sdp."EnglishProductName", sdps."EnglishProductSubcategoryName", sdpc."EnglishProductCategoryName"
	from "stg_DimProduct" sdp
	left join "stg_DimProductSubcategory" sdps
		on sdp."ProductSubcategoryKey" = sdps."ProductSubcategoryKey"
	left join "stg_DimProductCategory" sdpc
		on sdps."ProductCategoryKey" = sdpc."ProductCategoryKey") sdpc1
	on sfis."ProductKey" = sdpc1."ProductKey"
order by 1,2,3