import os

def set_hash_seed(seed: str) -> None:
  os.environ["PYTHONHASHSEED"] = seed
  
def hash_inputs(inputs: list[float], num_features: int) -> list[float]:
  # https://en.wikipedia.org/wiki/Feature_hashing#:~:text=In%20machine%20learning%2C%20feature%20hashing%2C%20also%20known%20as,features%20into%20indices%20in%20a%20vector%20or%20matrix.
  x = [0 for _ in range(num_features)]
  
  for i, item in enumerate(inputs):
    h = hash((i, item))
    x[h % num_features] += 1
    
  return x
