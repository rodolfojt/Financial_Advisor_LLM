# Financial Advisor

Chatbot built as Financial Advisor using 3-pipeline architecture. My focus on this project is to put into practice some important concepts in the Generative AI field, drawing from the Hands-On LLMs free course. By following this course, I've delved into various key areas such as:

- Deployment of a Large Language Model (LLM).
- Designing and building a Retrieval-Augmented Generation (RAG) system.
- Implementing LLMOps in practice to ensure efficient management and deployment of LLM-based models.
- Establishing my first Vector Database (DB), a crucial component for efficient data storage and retrieval.
- Constructing a streaming pipeline to handle real-time data processing.

This project serves as a practical exercise based on the course _Learn to Train and Deploy a Real-Time Financial Advisor_.

The source code used as a reference can be found [here](https://github.com/iusztinpaul/hands-on-llms/tree/main).

## Main Technologies Used

### Libraries

- **Transformers**: Leveraged for implementing Large Language Models (LLMs).
- **PyTorch**: Required for deep learning tasks; specifically version 2.0.1 was utilized.
- **Pydantic**: Utilized for data validation and settings management.
- **PyYAML**: Employed for configuration file parsing.
- **WebSocket Client**: Facilitates communication with WebSocket servers.
- **Python-dotenv**: Simplifies loading environment variables from `.env` files.

### Tools and Frameworks

- **Bytewax**: Integrated for deploying and managing serverless functions.
- **Qdrant-client**: Utilized for interaction with Qdrant vector database.
- **Fire**: Employed for building command-line interfaces (CLIs).

### Other Dependencies

- **Sentencepiece**: Used for text tokenization.
- **Unstructured**: Assists in handling unstructured data.
- **Ruff**: Integrated for code formatting and linting.
- **Black**: Utilized for code formatting.

These technologies are instrumental in realizing the 3-pipeline architecture and implementing various components of the financial advisor chatbot as outlined in the Hands-On LLMs course.
