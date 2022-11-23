import argparse

from flask import Flask, jsonify

from agent import EGreedyAgent, ThompsonAgent
from environment import Environment

AGENTS = {"egreedy": EGreedyAgent, "thompson": ThompsonAgent}


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bandits-number", type=int, required=True)
    parser.add_argument("--probabilities", type=float, nargs="+", required=True)
    parser.add_argument("--agent-cls", type=str, required=True)
    parser.add_argument("--epsilon", type=float, required=False)
    return parser


parser = create_parser()
args, _ = parser.parse_known_args()

environment = Environment(
    bandits_number=args.bandits_number, probabilities=args.probabilities
)

if args.agent_cls == "egreedy":
    agent = EGreedyAgent(environment=environment, epsilon=args.epsilon)
elif args.agent_cls == "thompson":
    agent = ThompsonAgent(environment=environment)
else:
    raise ValueError(f"Agent {args.agent_cls} is unknown")

app = Flask(__name__)


@app.route("/", methods=["GET"])
def make_action():
    bandit_number, reward = environment.action(agent)
    agent.update(bandit_number, reward)
    response = {
        "message": f"Action done, selected bandit number {bandit_number}",
        "selected bandits": list(environment.data["bandits"]),
        "received rewards": list(environment.data["rewards"]),
    }

    return jsonify(response), 200


app.run(host="0.0.0.0", port=5000)
