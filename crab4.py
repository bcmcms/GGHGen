from CRABClient.UserUtilities import config
config = config()

config.General.requestName   = 'GGHK1M_4'
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName = 'GGH_p4.py'
config.JobType.numCores = 4
config.JobType.maxMemoryMB = 4000
# This string determines the primary dataset of the newly-produced outputs.
# For instance, this dataset will be named /CrabTestSingleMu/something/USER
#config.Data.outputPrimaryDataset = 'CrabTestGGH2p2'
config.Data.inputDataset = '/CrabTestGGHK1M_2/mcmaster-CRAB3_MC_generation_GGHK1M_3r-889dc1528a7a51924818b24d55ffac27/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 25
#config.Data.totalUnits = 1000
config.Data.publication = True

# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'CRAB3_MC_generation_GGHK1M_4r2'

# Where the output files will be transmitted to
config.Site.storageSite = 'T3_US_Baylor'
