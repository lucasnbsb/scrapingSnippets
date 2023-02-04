/// <reference types="cypress" />

describe('scrapping redbubble for pictures of frogs', () => {
    beforeEach(() => {
        cy.visit('https://imgur.com/')
    })

    it('should visit the site and scroll to the bottom', () => {
        cy.scrollTo('bottom')
    })
})