from ai_providers.openai_client import ask_openai

class GoldAgent:
    def decide(self, strategy_signal, lstm_prediction):

        prompt = f"""
        Strategy suggests: {strategy_signal}
        LSTM predicted price: {lstm_prediction}
        Should we execute this trade? Respond with reasoning.
        """

        return ask_openai(prompt)
