from fastapi import FastAPI, File, Form, UploadFile
import zipfile
import csv
import io

app = FastAPI()

@app.post("/api/")
async def answer_question(
    question: str = Form(...),
    file: UploadFile = File(None)
):
    # Process optional file
    if file:
        try:
            # Extract ZIP file
            with zipfile.ZipFile(file.file) as z:
                for filename in z.namelist():
                    if filename.endswith('.csv'):
                        with z.open(filename) as csvfile:
                            csv_reader = csv.DictReader(io.TextIOWrapper(csvfile))
                            for row in csv_reader:
                                if "answer" in row:
                                    return {"answer": row["answer"]}
        except Exception as e:
            return {"answer": f"Error processing file: {str(e)}"}
    
    # Placeholder for LLM integration (to answer without file)
    # For now, return a static message.
    return {"answer": "LLM logic needs to be added here."}
    if __name__=="__main__":
        app.run()
#import openai

#def query_llm(question):
   # response = openai.Completion.create(
    #    engine="text-davinci-003",
     #   prompt=question,
      #  max_tokens=100
    #)
    #return response["choices"][0]["text"].strip()
#def generate_prompt(question, assignment_type=None):
 #   base_prompt = "You are answering questions for graded assignments."
  #  if assignment_type:
   #     base_prompt += f" This question belongs to {assignment_type}."
    # return f"{base_prompt}\n\nQuestion: {question}\nAnswer:"


