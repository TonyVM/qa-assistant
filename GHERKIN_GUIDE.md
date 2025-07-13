# Gherkin User Stories Examples

## What is Gherkin?

Gherkin is a domain-specific language that lets you describe software behavior without detailing how that functionality is implemented. It's written in a natural language style that can be read and understood by technical and non-technical team members.

## Basic Gherkin Syntax

- **Feature**: Describes the software feature being tested
- **Scenario**: Describes a specific test case
- **Given**: Describes the initial context
- **When**: Describes the action/event
- **Then**: Describes the expected outcome
- **And/But**: Adds additional conditions

## Example 1: E-commerce Login

```gherkin
Feature: User Authentication
  As a customer
  I want to log into my account
  So that I can access my personal information and order history

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter my valid email and password
    And I click the login button
    Then I should be redirected to my dashboard
    And I should see a welcome message

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter an invalid email or password
    And I click the login button
    Then I should see an error message
    And I should remain on the login page
```

## Example 2: Shopping Cart

```gherkin
Feature: Shopping Cart Management
  As a customer
  I want to manage items in my shopping cart
  So that I can purchase the products I want

  Scenario: Add item to empty cart
    Given my shopping cart is empty
    When I add a product to the cart
    Then the cart should contain 1 item
    And the cart total should reflect the product price

  Scenario: Remove item from cart
    Given my cart contains 2 items
    When I remove 1 item from the cart
    Then the cart should contain 1 item
    And the cart total should be updated accordingly
```

## Benefits of Gherkin Format

1. **Human-readable**: Both technical and non-technical team members can understand
2. **Executable**: Can be automated with tools like Cucumber, Behave, SpecFlow
3. **Living documentation**: Scenarios serve as documentation that stays up-to-date
4. **Collaboration**: Facilitates communication between developers, testers, and business analysts
5. **BDD approach**: Encourages behavior-driven development practices

## Best Practices

1. **Write from user perspective**: Focus on business value
2. **Keep scenarios simple**: One scenario per business rule
3. **Use domain language**: Avoid technical jargon
4. **Be declarative**: Describe what, not how
5. **Independent scenarios**: Each scenario should be able to run independently
