
## This project is the result of the final assignment of the "Automated Testing with Selenium and Python" [course](https://stepik.org/course/575/).

The project follows an approach based on the Page Object Model:

- All action and assertion methods are encapsulated within dedicated methods in the PageObject classes.
- All selectors are centrally managed in the locators.py file.
- No assert statements are present within the test bodies.

The project also supports language parameterization for test execution.

Throughout development, I diligently adhered to industry best practices, maintained proper commit conventions, and ensured logical code organization.

## Getting Started

1. Clone the repository:

    ```
    git clone https://github.com/dshstrng/stepik_final_task.git
    cd stepik_final_task
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Run the required tests:

    ```
    pytest -v --tb=line --language=en -m need_review
    ```
