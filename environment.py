import numpy as np


class Environment:
    """
    Base environment class
    """

    def __init__(self, bandits_number: int, probabilities: list):
        """
        Args:
            bandits_number: Number of one-armed bandits
            probabilities: Probabilities of receiving a reward for each bandit
        """
        self.bandits_number = bandits_number
        self.probabilities = probabilities
        self.data = {"bandits": [], "rewards": []}

    def action(self, agent):
        """
        This function returns a reward depending on the bandit chosen by the agent and his probability

        Args:
            agent: BaseAgent class object

        Returns:
            bandit_number: Number of the bandit chosen by the agent at the current step
            reward: Reward received on the current step
        """
        bandit_number = agent.choose_bandit()
        reward = np.random.binomial(1, self.probabilities[bandit_number])
        self.log_data(bandit_number, reward)
        return bandit_number, reward

    def log_data(self, bandit_number, reward):
        """
        This function logs the number of the selected bandit and the reward received at the current step
        Args:
            bandit_number: Number of the bandit chosen by the agent at the current step
            reward: Reward received on the current step
        """
        self.data["bandits"].append(int(bandit_number))
        self.data["rewards"].append(int(reward))
