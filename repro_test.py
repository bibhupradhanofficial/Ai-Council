
import sys
import os

# Add project root to sys.path
sys.path.append(os.getcwd())

from ai_council.core.models import AgentResponse, SelfAssessment, RiskLevel
from ai_council.synthesis.layer import SynthesisLayerImpl

def test_repro():
    synthesis_layer = SynthesisLayerImpl()
    
    resp_low = AgentResponse(
        subtask_id="1", model_used="a", content="c", success=True,
        self_assessment=SelfAssessment(confidence_score=1.0, risk_level=RiskLevel.LOW)
    )
    resp_high = AgentResponse(
        subtask_id="1", model_used="b", content="c2", success=True,
        self_assessment=SelfAssessment(confidence_score=1.0, risk_level=RiskLevel.HIGH)
    )
    
    conf = synthesis_layer._calculate_overall_confidence([resp_low, resp_high])
    print(f"Calculated confidence: {conf}")
    print(f"Expected: 0.98")
    
    # Check intermediate values
    total_confidence = 0.0
    total_weight = 0.0
    risk_weights = {'low': 1.0, 'medium': 0.8, 'high': 0.6, 'critical': 0.4}
    
    for r in [resp_low, resp_high]:
        confidence = r.self_assessment.confidence_score
        weight = risk_weights.get(r.self_assessment.risk_level.value, 0.5)
        print(f"Response model={r.model_used}, confidence={confidence}, risk={r.self_assessment.risk_level.value}, weight={weight}")
        total_confidence += confidence * weight
        total_weight += weight
    
    weighted_avg = total_confidence / total_weight
    print(f"Weighted average: {weighted_avg}")
    
    penalty = min(0.1, (2 - 1) * 0.02)
    print(f"Penalty: {penalty}")
    final = weighted_avg - penalty
    print(f"Final: {final}")

if __name__ == "__main__":
    test_repro()
