import FWCore.ParameterSet.Config as cms

configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('$Revision$'),
	name = cms.untracked.string('$Source$'),
	annotation = cms.untracked.string('Spring10: Pythia8 generation of QCD events, 7TeV, pthat = 300 .. 380 GeV')
)

generator = cms.EDFilter("Pythia8GeneratorFilter",
	crossSection = cms.untracked.double(9.593e+02),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaPylistVerbosity = cms.untracked.int32(1),
	filterEfficiency = cms.untracked.double(1.0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	comEnergy = cms.double(7000.0),
	PythiaParameters = cms.PSet(
		processParameters = cms.vstring(
			'Main:timesAllowErrors    = 10000',
			'ParticleDecays:limitTau0 = on',
			'ParticleDecays:tauMax = 10',
			'HardQCD:all = on',
			'PhaseSpace:pTHatMin = 300',
			'PhaseSpace:pTHatMax = 380',
			'Tune:pp 2',
			'Tune:ee 3'),
		parameterSets = cms.vstring('processParameters')
	)
)