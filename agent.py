import numpy as np


class BaseAgent:
    """
    Basic class for agents
    """

    def __init__(self, environment):
        """
        Args:
            environment: Environment class object
        """
        self.bandits = np.arange(0, environment.bandits_number)
        self.rewards = np.ones(environment.bandits_number)
        self.attempts = np.ones(environment.bandits_number)


class EGreedyAgent(BaseAgent):
    """
    Epsilon Greedy Agent Implementation
    """

    def __init__(self, environment, epsilon: float = 0.1):
        """
        Args:
            environment: Environment class object
            epsilon: The probability of choosing the bandit with the highest expected reward
        """
        super().__init__(environment)
        self.epsilon = epsilon
        self.expected_rewards = np.ones(environment.bandits_number)

    def choose_bandit(self):
        """
        This function selects a bandit based on the epsilon probability

        Returns:
            bandit_number: Number of the bandit chosen by the agent at the current step
        """
        flag = np.random.binomial(1, self.epsilon)
        if flag == 0:
            bandit_number = np.random.choice(self.bandits)
        else:
            bandit_number = np.argmax(self.expected_rewards)
        return bandit_number

    def update(self, bandit_number, reward):
        """
        This function updates the agent parameters based on the results of the current step

        Args:
            bandit_number: Number of the bandit chosen by the agent at the current step
            reward: Reward received on the current step
        """
        self.attempts[bandit_number] += 1 - reward
        self.rewards[bandit_number] += reward
        self.expected_rewards = self.rewards / self.attempts


class ThompsonAgent(BaseAgent):
    """
    Thompson Sampling Agent Implementation
    """

    def __init__(self, environment):
        """
        Args:
            environment: Environment class object
        """
        super().__init__(environment)
        self.theta = np.zeros(environment.bandits_number)

    def choose_bandit(self):
        """
        This function samples theta values based on the beta distributions of the environment parameters,
        and then selects the bandit with the maximum theta value

        Returns:
            bandit_number: Number of the bandit chosen by the agent at the current step
        """
        self.theta = np.random.beta(self.rewards, self.attempts)
        bandit_number = np.argmax(self.theta)
        return bandit_number

    def update(self, bandit_number: int, reward: int):
        """
        This function updates the agent parameters based on the results of the current step

        Args:
            bandit_number: Number of the bandit chosen by the agent at the current step
            reward: Reward received on the current step
        """
        self.attempts[bandit_number] += 1 - reward
        self.rewards[bandit_number] += reward
