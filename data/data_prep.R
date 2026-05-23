library(tidyverse)

college_csv <- read_csv("MERGED2024_25_PP.csv")

colleges <- college_csv %>%
	 select(INSTNM, CITY, STABBR, REGION, LOCALE, CONTROL, ADM_RATE, ACTCM25, ACTCM75, SATMT25, SATMT75, SATVR25,SATVR75, UGDS, NPT4_PUB, NPT4_PRIV, NPT41_PUB, NPT42_PUB, NPT43_PUB, NPT44_PUB, NPT45_PUB, NPT41_PRIV, NPT42_PRIV, NPT43_PRIV, NPT44_PRIV, NPT45_PRIV, GRAD_DEBT_MDN, C150_4, MD_EARN_WNE_P10, starts_with("PCIP"))

clean_college <- colleges %>%
	      filter(!is.na(ADM_RATE), !is.na(UGDS), !is.na(C150_4), !is.na(NPT4_PUB) | !is.na(NPT4_PRIV))

