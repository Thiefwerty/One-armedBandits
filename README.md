# One-armedBandits
 One-armedBandits problem realization with E-Greedy and Thompson Sampling alghoritms
## Getting started

```bash
git clone https://github.com/Thiefwerty/One-armedBandits.git && cd One-armedBandits
pip install -r requirements.txt
bash run_app.sh

# alternatively, you could use docker
docker build . -t <image_name>:<tag_name>
docker run <image_name>:<tag_name>
```
## Change arguments

To configure the environment and agent parameters, you must specify the values of the variables in *run_app.sh*
```bibtex
--agent-cls - class of the used algorithm
    egreedy for Epsilon Greedy Alghoritm
    thompson Thompson Sampling Alghoritm
    
--bandits-number - number of bandit in envinronment

--probabilities - probabilities list of receiving reward for each bandit

--epsilon - epsilon probability value for Epsilon Greedy Alghoritm.
    Required only if --agent-cls egreedy
```