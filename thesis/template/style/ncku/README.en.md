<!-- doc-pair: ncku-department-catalogue; lang: en; topics: scope,generic-institution-api,ncku-college-presets,ncku-department-presets,other-institution-boundary -->

[繁體中文](README.md) | [English](README.en.md)

# NCKU college and department API catalogue

## Scope

This catalogue is derived from the current tracked source: [`college.tex`](college.tex) provides 9 NCKU college presets and [`department.tex`](department.tex) provides 110 NCKU department presets. “Department” is the cover metadata slot name; the catalogue actually includes departments, graduate institutes, degree programs, and centers rather than one strict organization type. Each preset sets the unit values and one NCKU college. These commands are the template's preserved NCKU convenience catalogue, not an authoritative current university organization list. Verify current NCKU and unit names and rules before use.

## Generic institution API

The shared command layer defines these APIs for every profile.

| Setter | Stored values | Getters |
| --- | --- | --- |
| `\SetUniversityName{Chinese university name}{English university name}` | Chinese and English university names | `\GetUniversityChiName`, `\GetUniversityEngName` |
| `\SetCollName{Chinese college name}{English college name}` | Chinese and English college names | `\GetCollChiName`, `\GetCollEngName` |
| `\SetDeptName{Chinese department name}{English abbreviation}{English full name}` | Chinese department name, English abbreviation, and English full name | `\GetDeptChiName`, `\GetDeptEngShortName`, `\GetDeptEngName` |

NCKU presets are shortcuts around these generic setters. The second `\SetDeptName` argument is returned by `\GetDeptEngShortName`; the third is returned by `\GetDeptEngName`.

## NCKU college presets

| Command | Chinese value | English value |
| --- | --- | --- |
| `\SetCollegeLiberalArts` | `文學院` | `College of Liberal Arts` |
| `\SetCollegeSciences` | `理學院` | `College of Sciences` |
| `\SetCollegeEngineering` | `工學院` | `College of Engineering` |
| `\SetCollegeElectricalEngineeringAndComputerScience` | `電機資訊學院` | `College of Electrical Engineering and Computer Science` |
| `\SetCollegeManagement` | `管理學院` | `College of Management` |
| `\SetCollegeSocialScience` | `社會科學院` | `College of Social Science` |
| `\SetCollegePlanningAndDesign` | `規劃與設計學院` | `College of Planning and Design` |
| `\SetCollegeBioscienceAndBiotechnology` | `生物科學與科技學院` | `College of Bioscience and Biotechnology` |
| `\SetCollegeMedicine` | `醫學院` | `College of Medicine` |

## NCKU department presets

Each command below writes the department values and calls the listed college preset.

### College of Liberal Arts (`\SetCollegeLiberalArts`) — 8 presets

| Command | Chinese value | English abbreviation | English full value |
| --- | --- | --- | --- |
| `\SetDeptChinese` | `中國文學系` | `Chinese` | `Department of Chinese Literature` |
| `\SetDeptArt` | `藝術研究所` | `Art` | `Institute of Art` |
| `\SetDeptMinNan` | `閩南文化研究中心` | `MinNan` | `Min-Nan Culture Studies Center` |
| `\SetDeptFLLD` | `外國語文學系` | `FLLD` | `Department of Foreign Languages and Literature` |
| `\SetDeptTWL` | `臺灣文學系` | `TWL` | `Department of Taiwanese Literature` |
| `\SetDeptKCLC` | `華語中心` | `KCLC` | `Chinese Language Center` |
| `\SetDeptLang` | `外語中心` | `Lang` | `Foreign Language Center` |
| `\SetDeptHis` | `歷史學系` | `His` | `Department of History` |

### College of Sciences (`\SetCollegeSciences`) — 7 presets

| Command | Chinese value | English abbreviation | English full value |
| --- | --- | --- | --- |
| `\SetDeptMath` | `數學系` | `Math` | `Department of Mathematics` |
| `\SetDeptDPS` | `光電科學與工程學系` | `DPS` | `Department of Photonics` |
| `\SetDeptPhys` | `物理學系` | `Phys` | `Department of Physics` |
| `\SetDeptCh` | `化學系` | `Ch` | `Department of Chemistry` |
| `\SetDeptEarth` | `地球科學系` | `Earth` | `Department of Earth Sciences` |
| `\SetDeptPSSC` | `太空與電漿科學研究所` | `PSSC` | `Institute of Space and Plasma Sciences` |
| `\SetDeptNCTS` | `國家理論科學研究中心` | `NCTS` | `National Center for Theoretical Sciences (South)` |

### College of Engineering (`\SetCollegeEngineering`) — 18 presets

| Command | Chinese value | English abbreviation | English full value |
| --- | --- | --- | --- |
| `\SetDeptME` | `機械工程學系` | `ME` | `Department of Mechanical Engineering` |
| `\SetDeptChe` | `化學工程學系` | `Che` | `Department of Chemical Engineering` |
| `\SetDeptCivil` | `土木工程學系` | `Civil` | `Department of Civil Engineering` |
| `\SetDeptMSE` | `材料科學及工程學系` | `MSE` | `Department of Materials Science and Engineering` |
| `\SetDeptHyd` | `水利及海洋工程學系` | `Hyd` | `Department of Hydraulic and Ocean Engineering` |
| `\SetDeptES` | `工程科學系` | `ES` | `Department of Engineering Science` |
| `\SetDeptSNAME` | `系統及船舶機電工程學系` | `SNAME` | `Department of System and Naval Mechatronic Engineering` |
| `\SetDeptIAA` | `航空太空工程學系` | `IAA` | `Department of Aeronautics and Astronautics` |
| `\SetDeptMP` | `資源工程學系` | `MP` | `Department of Resources Engineering` |
| `\SetDeptEV` | `環境工程學系` | `EV` | `Department of Environmental Engineering` |
| `\SetDeptBME` | `生物醫學工程學系` | `BME` | `Department of BioMedical Engineering` |
| `\SetDeptGeomatics` | `測量及空間資訊學系` | `Geomatics` | `Department of Geomatics` |
| `\SetDeptIOTMA` | `海洋科技與事務研究所` | `IOTMA` | `Institute of Ocean Technology and Marine Affairs` |
| `\SetDeptICA` | `民航研究所` | `ICA` | `Institute of Civil Aviation` |
| `\SetDeptIBDPE` | `能源國際學士學位學程` | `IBDPE` | `International Bachelor Degree Program on Energy` |
| `\SetDeptICAMP` | `尖端材料國際碩士學位學程` | `ICAMP` | `International Curriculum for Advanced Materials Program` |
| `\SetDeptINHMM` | `自然災害減災及管理國際碩士學位學程` | `INHMM` | `International Master Program on \\ Natural Hazards Mitigation and Management` |
| `\SetDeptICEM` | `工程管理碩士在職專班` | `ICEM` | `International Graduate Program of \\ Civil Engineering and Management` |

### College of Electrical Engineering and Computer Science (`\SetCollegeElectricalEngineeringAndComputerScience`) — 6 presets

| Command | Chinese value | English abbreviation | English full value |
| --- | --- | --- | --- |
| `\SetDeptEE` | `電機工程學系` | `EE` | `Department of Electrical Engineering` |
| `\SetDeptCSIE` | `資訊工程研究所` | `CSIE` | `Institute of Computer Science and \\ Information Engineering` |
| `\SetDeptIME` | `微電子工程研究所` | `IME` | `Institute of Microelectronics` |
| `\SetDeptCCE` | `電腦與通信工程研究所` | `CCE` | `Institute of Computer \& Communication Engineering` |
| `\SetDeptIMIS` | `製造資訊與系統研究所` | `IMIS` | `Institute of Manufacturing Information and Systems` |
| `\SetDeptIMI` | `醫學資訊研究所` | `IMI` | `Institute of Medical Informatics` |

### College of Management (`\SetCollegeManagement`) — 12 presets

| Command | Chinese value | English abbreviation | English full value |
| --- | --- | --- | --- |
| `\SetDeptSTAT` | `統計學系` | `STAT` | `Department of Statistics` |
| `\SetDeptIDS` | `數據科學研究所` | `IDS` | `Institute of Data Science` |
| `\SetDeptACC` | `會計學系` | `ACC` | `Department of Accountancy` |
| `\SetDeptTCM` | `交通管理科學系` | `TCM` | `Department of Transportation and Communication Management Science` |
| `\SetDeptMBA` | `企業管理學系` | `MBA` | `Master of Business Administration` |
| `\SetDeptTM` | `電信管理研究所` | `TM` | `Institute of Telecommunications Management` |
| `\SetDeptIIM` | `工業與資訊管理學系暨資訊管理研究所` | `IIM` | `Institute of Information Management` |
| `\SetDeptFin` | `財務金融研究所` | `Fin` | `Institute of Finance \& Banking` |
| `\SetDeptPHEI` | `體育健康與休閒研究所` | `PHEI` | `Institute of Physical Education, \\ Health \& Leisure Studies` |
| `\SetDeptEMBA` | `高階管理碩士在職專班` | `EMBA` | `Executive Master of Business Administration` |
| `\SetDeptIMBA` | `國際經營管理研究所` | `IMBA` | `Institute of International Management` |
| `\SetDeptAMBA` | `經營管理碩士班` | `AMBA` | `Advanced Master of Business Administration` |

### College of Social Science (`\SetCollegeSocialScience`) — 8 presets

| Command | Chinese value | English abbreviation | English full value |
| --- | --- | --- | --- |
| `\SetDeptPolSci` | `政治學系` | `PolSci` | `Department of Political Science` |
| `\SetDeptEconomic` | `經濟學系` | `Economic` | `Department of Economics` |
| `\SetDeptPsychology` | `心理學系` | `Psychology` | `Department of Psychology` |
| `\SetDeptLaw` | `法律學系` | `Law` | `Department of Law and \\Institute of Law in Science and Technology` |
| `\SetDeptED` | `教育研究所` | `ED` | `Institute of Education` |
| `\SetDeptIOCS` | `認知科學研究所` | `IOCS` | `Institute of Cognitive Science` |
| `\SetDeptGIPE` | `政治經濟學研究所` | `GIPE` | `Institute of Political Economy` |
| `\SetDeptFMRI` | `心智影像研究中心` | `FMRI` | `Mind Research and Image Center` |

### College of Planning and Design (`\SetCollegePlanningAndDesign`) — 4 presets

| Command | Chinese value | English abbreviation | English full value |
| --- | --- | --- | --- |
| `\SetDeptArch` | `建築學系` | `Arch` | `Department of Architecture` |
| `\SetDeptUP` | `都市計劃學系` | `UP` | `Department of Urban Planning` |
| `\SetDeptID` | `工業設計學系` | `ID` | `Department of Industrial Design` |
| `\SetDeptICID` | `創意產業設計研究所` | `ICID` | `Institute of Creative Industry Design` |

### College of Bioscience and Biotechnology (`\SetCollegeBioscienceAndBiotechnology`) — 4 presets

| Command | Chinese value | English abbreviation | English full value |
| --- | --- | --- | --- |
| `\SetDeptBio` | `生命科學系` | `Bio` | `Department of Life Sciences` |
| `\SetDeptBioTech` | `生物科技研究所` | `BioTech` | `Institute of Biotechnology` |
| `\SetDeptIBBT` | `生物資訊與訊息傳遞研究所` | `IBBT` | `Institute of Bioinformatics and \\ Biosignal Transduction` |
| `\SetDeptITPS` | `熱帶植物科學研究所` | `ITPS` | `Institute of Tropical Plant Sciences` |

### College of Medicine (`\SetCollegeMedicine`) — 43 presets

| Command | Chinese value | English abbreviation | English full value |
| --- | --- | --- | --- |
| `\SetDeptEDUC` | `醫學系` | `EDUC` | `School of Medicine` |
| `\SetDeptBiohem` | `生物化學暨分子生物學研究所` | `Biohem` | `Department of Biochemistry and \\ Molecular Biology` |
| `\SetDeptPath` | `病理學科` | `Path` | `Department of Pathology` |
| `\SetDeptIntMed` | `內科學科` | `IntMed` | `Department of Internal Medicine` |
| `\SetDeptPhysMed` | `生理學研究所` | `PhysMed` | `Department of Physiology` |
| `\SetDeptSurgery` | `外科學科` | `Surgery` | `Department of Surgery` |
| `\SetDeptPed` | `小兒學科` | `Ped` | `Department of Pediatrics` |
| `\SetDeptAnatomy` | `解剖學科暨細胞生物與解剖學研究所` | `Anatomy` | `Department of Cell Biology and Anatomy` |
| `\SetDeptObsGyn` | `婦產學科` | `ObsGyn` | `Department of Obstetrics and Gynecology` |
| `\SetDeptBone` | `骨科學科` | `Bone` | `Department of Orthopaedics` |
| `\SetDeptPhMed` | `公共衛生學科暨公共衛生研究所` | `PhMed` | `Department of Public Health` |
| `\SetDeptNeuro` | `神經學科` | `Neuro` | `Department of Neurology` |
| `\SetDeptPsy` | `精神學科` | `Psy` | `Department of Psychiatry` |
| `\SetDeptParasite` | `寄生蟲學科` | `Parasite` | `Department of Parasitology` |
| `\SetDeptOphth` | `眼科學科` | `Ophth` | `Department of Ophthalmology` |
| `\SetDeptOtolaryngo` | `耳鼻喉學科` | `Otolaryngo` | `Department of Otolaryngology` |
| `\SetDeptDEOH` | `工業衛生學科暨環境醫學研究所` | `DEOH` | `Department of Environmental and Occupational Health` |
| `\SetDeptDerm` | `皮膚學科` | `Derm` | `Department of Dermatology` |
| `\SetDeptUro` | `泌尿學科` | `Uro` | `Department of Urology` |
| `\SetDeptPharmaco` | `藥理學科暨藥理學研究所` | `Pharmaco` | `Department of Pharmacology` |
| `\SetDeptAnesth` | `麻醉學科` | `Anesth` | `Department of Anesthesiology` |
| `\SetDeptRehab` | `復健學科` | `Rehab` | `Department of Physical Medicine and Rehabilitation` |
| `\SetDeptMicrobio` | `微生物學及免疫研究所` | `Microbio` | `Department of Microbiology and Immunology` |
| `\SetDeptRad` | `放射線學科` | `Rad` | `Department of Diagnostic Radiology` |
| `\SetDeptNM` | `核子醫學科` | `NM` | `Department of Nuclear Medicine` |
| `\SetDeptFamily` | `家庭醫學科` | `Family` | `Department of Family Medicine` |
| `\SetDeptEmergency` | `急診學科` | `Emergency` | `Department of Emergency Medicine` |
| `\SetDeptDentistry` | `牙科學科` | `Dentistry` | `Department of Dentistry` |
| `\SetDeptOEM` | `職業及環境醫學科` | `OEM` | `Department of Occupational and Environmental Medicine` |
| `\SetDeptForensic` | `法醫學科` | `Forensic` | `Department of Forensic Medicine` |
| `\SetDeptNursing` | `護理學系` | `Nursing` | `Department of Nursing` |
| `\SetDeptMT` | `醫學檢驗生物技術學系` | `MT` | `Department of Medical Laboratory \\Science and Biotechnology` |
| `\SetDeptPT` | `物理治療學系` | `PT` | `Department of Physical Therapy` |
| `\SetDeptOT` | `職能治療學系` | `OT` | `Department of Occupational Therapy` |
| `\SetDeptPharmacy` | `藥學系` | `Pharmacy` | `School of Pharmacy` |
| `\SetDeptBasicMed` | `基礎醫學研究所` | `BasicMed` | `Institute of Basic Medical Sciences` |
| `\SetDeptBehMed` | `行為醫學研究所` | `BehMed` | `Institute of Behavioral Medicine` |
| `\SetDeptCLPARM` | `臨床藥學與藥物科技研究所` | `CLPARM` | `Institute of Clinical Pharmacy \\ and Pharmaceutical Sciences` |
| `\SetDeptIMM` | `分子醫學研究所` | `IMM` | `Institute of Molecular Medicine` |
| `\SetDeptIOM` | `口腔醫學研究所` | `IOM` | `Institute of Oral Medicine` |
| `\SetDeptICMMed` | `臨床醫學研究所` | `ICMMed` | `Institute of Clinical Medicine` |
| `\SetDeptAlliedHealth` | `健康照護科學研究所` | `AlliedHealth` | `Institute of Allied Health Sciences` |
| `\SetDeptIOG` | `老年學研究所` | `IOG` | `Institute of Gerontology` |

## Students from other institutions

Only the `ncku` profile loads these NCKU commands; `custom` and another institution profile use the generic setters directly. A reusable catalogue uses institution-prefixed commands (for example, `\SetNTUDept...`) rather than reusing NCKU `\SetDept...` names. See [`../Customization.en.md`](../Customization.en.md) for the complete workflow and illustrative NTU wiring.
