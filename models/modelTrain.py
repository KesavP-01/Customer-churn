from models.model import churnModel
import joblib as jl

if __name__ == "__main__":

    model = churnModel('data/Churn.csv')

    jl.dump(model, 'models/churnModel')