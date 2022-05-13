* import spatial information
spshape2dta tl_2018_us_county
use tl_2018_us_county, clear
br
generate long fips = real(STATEFP + COUNTYFP)
bysort fips : assert _N == 1
assert fips != .
spset fips, modify replace
spset, modify coordsys(latlong, miles)


* import main data
clear all
cd "F:\research projects\widss"
import delimited "C:\Users\xwang222\Downloads\dataset.csv"

merge 1:1 fips using tl_2018_us_county
keep if _merge == 3

spmatrix create contiguity W, replace

export delimited using "F:\research projects\widss\MasterData.csv", replace

global output="F:\research projects\widss\"
global FileName ="Reg_t1_220513"

local variables totalnursepractitioners2019 totalphysicianassistants2019 totalhospitals2019 internalmedicineprimarycare2019 familymedicinegeneralpracticepri totalspecialistphysicians2019 icubeds_x
foreach m of local variables{

reg `m' unemployment_rate_2018 percentofpopulationaged60 percentofadultswithabachelorsdeg blackalone povall_2018,
outreg2 using "$output\$FileName.xls", excel dec(3) label 

spregress `m' unemployment_rate_2018 percentofpopulationaged60 percentofadultswithabachelorsdeg blackalone povall_2018, dvarlag(W) gs2sls force
outreg2 using "$output\$FileName.xls", excel dec(3) label 


}