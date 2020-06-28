from CRABClient.UserUtilities import config
config = config()

config.General.requestName   = 'GGHK1M_2'
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName = 'GGH_p2.py'
config.JobType.numCores = 1
config.JobType.maxMemoryMB = 4000
# This string determines the primary dataset of the newly-produced outputs.
# For instance, this dataset will be named /CrabTestSingleMu/something/USER
config.Data.outputPrimaryDataset = 'CrabTestGGHK1M_2'
config.Data.userInputFiles = open('/eos/uscms/store/user/mcmaster/GGH1.txt').readlines()
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 100
config.Data.publication = True

# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'CRAB3_MC_generation_GGHK1M_2'

# Where the output files will be transmitted to
config.Site.storageSite = 'T3_US_Baylor'
