from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
import pandas as pd

# Load base model (VERY IMPORTANT)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load CSV
df = pd.read_csv("training_data.csv")

train_examples = []

for _, row in df.iterrows():
    train_examples.append(
        InputExample(
            texts=[row["job_description"], row["model_response"]],
            label=1.0
        )
    )

train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=8)

train_loss = losses.CosineSimilarityLoss(model)

# Train
model.fit(
    train_objectives=[(train_dataloader, train_loss)],
    epochs=1,
    warmup_steps=100
)

# ✅ SAVE PROPERLY
model.save("resume_ats_model")

print("Model training complete & saved correctly")
