import FWCore.ParameterSet.Config as cms

process = cms.Process("TESTPROD")
process.load("FWCore.Framework.test.cmsExceptionsFatal_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(15)
)
process.Thing = cms.EDProducer("ThingProducer",
    debugLevel = cms.untracked.int32(0)
)

process.OtherOtherThing = cms.EDProducer("OtherThingProducer",
    debugLevel = cms.untracked.int32(0)
)

process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('keep *', 
        'drop *_OtherOtherThing_*_*'),
    fileName = cms.untracked.string('file:FastMergeTest_2.root')
)

process.source = cms.Source("EmptySource",
    firstEvent = cms.untracked.uint32(100),
    firstRun = cms.untracked.uint32(200)
)

process.p = cms.Path(process.Thing*process.OtherOtherThing)
process.ep = cms.EndPath(process.output)


