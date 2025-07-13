# 🥒 Gherkin User Stories Demo

## Overview

Esta demo muestra la nueva funcionalidad de **Gherkin User Stories** en QA Assistant v1.2.0-beta, que permite generar historias de usuario en formato BDD (Behavior Driven Development).

## ¿Qué es Gherkin?

Gherkin es un lenguaje específico de dominio que te permite describir el comportamiento del software sin detallar cómo se implementa esa funcionalidad. Está escrito en un estilo de lenguaje natural que pueden leer y entender tanto miembros técnicos como no técnicos del equipo.

## Ejemplo de Uso

### Entrada: Documento PDF con Requerimientos

```
Sistema de E-commerce

1. Autenticación de Usuario
   - Los usuarios deben poder registrarse con email y contraseña
   - Los usuarios deben poder iniciar sesión en su cuenta
   - Los usuarios deben poder recuperar su contraseña

2. Gestión de Carrito de Compras
   - Los usuarios deben poder agregar productos al carrito
   - Los usuarios deben poder modificar cantidades en el carrito
   - Los usuarios deben poder eliminar productos del carrito

3. Proceso de Checkout
   - Los usuarios deben poder ingresar información de envío
   - Los usuarios deben poder seleccionar método de pago
   - Los usuarios deben poder revisar y confirmar su pedido
```

### Salida: Gherkin User Stories Generadas

```gherkin
Feature: User Authentication
  As a customer
  I want to authenticate to the system
  So that I can access my personal account and shopping features

  Scenario: Successful user registration
    Given I am on the registration page
    When I enter a valid email address
    And I enter a strong password
    And I confirm my password
    And I click the register button
    Then I should see a confirmation message
    And I should receive a verification email

  Scenario: Successful login with valid credentials
    Given I am on the login page
    And I have a registered account
    When I enter my valid email and password
    And I click the login button
    Then I should be redirected to my dashboard
    And I should see a welcome message

  Scenario: Password recovery
    Given I am on the login page
    When I click the "Forgot Password" link
    And I enter my registered email address
    And I click the send recovery email button
    Then I should see a confirmation message
    And I should receive a password recovery email

Feature: Shopping Cart Management
  As a customer
  I want to manage items in my shopping cart
  So that I can control what I purchase

  Scenario: Add product to empty cart
    Given my shopping cart is empty
    And I am viewing a product page
    When I click the "Add to Cart" button
    Then the product should be added to my cart
    And the cart counter should show 1 item
    And the cart total should reflect the product price

  Scenario: Modify product quantity in cart
    Given I have products in my shopping cart
    And I am viewing my cart
    When I increase the quantity of a product
    Then the cart should update the quantity
    And the total price should be recalculated
    And the cart should save my changes

  Scenario: Remove product from cart
    Given I have multiple products in my cart
    And I am viewing my cart
    When I click the remove button for a specific product
    Then the product should be removed from my cart
    And the cart total should be updated
    And the cart counter should decrease

Feature: Checkout Process
  As a customer
  I want to complete my purchase
  So that I can receive the products I selected

  Scenario: Complete checkout with valid information
    Given I have products in my cart
    And I am on the checkout page
    When I enter valid shipping information
    And I select a payment method
    And I review my order details
    And I confirm my purchase
    Then my order should be processed
    And I should receive an order confirmation
    And I should see an order confirmation page

  Scenario: Checkout validation for required fields
    Given I have products in my cart
    And I am on the checkout page
    When I try to proceed without entering shipping information
    Then I should see validation error messages
    And I should not be able to complete the purchase
    And I should remain on the checkout page
```

## Beneficios del Formato Gherkin

### 1. **Legibilidad Universal**
- Técnicos y no técnicos pueden entender los scenarios
- Sintaxis clara con Given/When/Then
- Enfoque en el comportamiento del usuario

### 2. **Ejecutabilidad**
- Compatible con frameworks BDD como:
  - **Cucumber** (Java, JavaScript, Ruby)
  - **Behave** (Python)
  - **SpecFlow** (.NET)
  - **Gherkin** (multi-lenguaje)

### 3. **Documentación Viva**
- Los scenarios sirven como documentación ejecutable
- Se mantienen actualizados con el código
- Facilitan la comunicación entre equipos

### 4. **Automatización de Pruebas**
- Los scenarios se pueden automatizar directamente
- Permiten desarrollo guiado por comportamiento (BDD)
- Mejoran la cobertura de pruebas

## Exportación a CSV

La aplicación exporta los Gherkin User Stories en formato CSV estructurado:

| Feature | User Story | Scenario | Steps |
|---------|------------|----------|-------|
| User Authentication | As a customer I want to authenticate... | Successful user registration | Given I am on the registration page \| When I enter a valid email... |
| User Authentication | As a customer I want to authenticate... | Successful login with valid credentials | Given I am on the login page \| When I enter my valid email... |
| Shopping Cart Management | As a customer I want to manage items... | Add product to empty cart | Given my shopping cart is empty \| When I click the "Add to Cart"... |

## Casos de Uso Ideales

### 1. **Equipos BDD**
- Desarrollo guiado por comportamiento
- Colaboración entre Product Owners, Developers y QA

### 2. **Documentación de Requerimientos**
- Especificaciones ejecutables
- Documentación que no se vuelve obsoleta

### 3. **Automatización de Pruebas**
- Framework para pruebas automatizadas
- Integración con pipelines CI/CD

### 4. **Comunicación Stakeholder**
- Lenguaje común entre negocio y técnicos
- Scenarios claros y verificables

## Nuevas Características en v1.2.0-beta

- ✅ **Generación de Gherkin**: Nuevo tipo de artefacto disponible
- ✅ **Parser especializado**: Análisis inteligente de Features y Scenarios
- ✅ **Exportación CSV**: Formato estructurado para Gherkin
- ✅ **Documentación completa**: Guías y ejemplos incluidos
- ✅ **Integración perfecta**: Se integra con la arquitectura LangChain existente

## Próximos Pasos

1. **Probar la funcionalidad** con documentos reales
2. **Integrar con herramientas BDD** existentes
3. **Automatizar scenarios** generados
4. **Crear documentación viva** para tus proyectos

¡La nueva funcionalidad de Gherkin User Stories hace que QA Assistant sea la herramienta perfecta para equipos que implementan Behavior Driven Development! 🚀
