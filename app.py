from agents.gold_agent import GoldAgent

def run_fte():
    agent = GoldAgent()
    decision = agent.decide("BUY", 2350.50)
    print("AI Decision:", decision)

if __name__ == "__main__":
    run_fte()
