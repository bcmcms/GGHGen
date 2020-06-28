from CRABClient.UserUtilities import config
config = config()

config.General.requestName   = 'GGHK1M'
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
# Name of the CMSSW configuration file
config.JobType.psetName = 'GGH_p1.py'
config.JobType.numCores = 1
config.JobType.inputFiles = ['ggh01_M1225_Toa01a01_M9_Tobbbb_tarball.tar.xz']

# This string determines the primary dataset of the newly-produced outputs.
# For instance, this dataset will be named /CrabTestSingleMu/something/USER
config.Data.outputPrimaryDataset = 'CrabTestGGHK1M'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 200
config.Data.totalUnits = 1000000
config.Data.publication = True

# This string is used to construct the output dataset name
config.Data.outputDatasetTag = 'CRAB3_MC_generation_GGHK1M'

# Where the output files will be transmitted to
config.Site.storageSite = 'T3_US_Baylor'
