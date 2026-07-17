# Python Collections Comparison

| Data structure | Ordered? | Mutable? | Allows duplicates? | Use case |
|---|---|---|---|---|
| List | Yes | Yes | Yes | When you need an ordered collection that may change, like a to-do list or shopping cart. |
| Tuple | Yes | No | Yes | When you need fixed data that should not change, like coordinates or a record. |
| Set | No | Yes | No | When you need unique items only, like removing duplicates or checking membership quickly. |
| Dictionary | Yes, as of modern Python versions | Yes | Keys: no, values: yes | When you need key-value pairs, like storing student details or settings. |

## Simple theory

- List: best for changing ordered data.
- Tuple: best for fixed ordered data.
- Set: best for unique unordered data.
- Dictionary: best for labeled data using keys and values.

One important detail: in dictionaries, keys must be unique, but values can repeat.