from pipeline.data_loader import load_data
from pipeline.preprocess import preprocess
from pipeline.train import train_model
from pipeline.evaluate import evaluate_model
from pipeline.save_model import save_model

def run_pipeline():
    print("📥 Loading data...")
    df = load_data("data/sample.csv")

    print("🧹 Preprocessing data...")
    X_train, X_test, y_train, y_test = preprocess(df)

    print("🧠 Training model...")
    model = train_model(X_train, y_train)

    print("📊 Evaluating model...")
    score = evaluate_model(model, X_test, y_test)
    print(f"✅ Model Accuracy: {round(score, 3)}")

    print("💾 Saving model...")
    save_model(model, "models/model.pkl")

    print("🚀 Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
