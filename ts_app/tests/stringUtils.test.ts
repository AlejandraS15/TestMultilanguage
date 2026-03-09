import { describe, it, expect } from 'vitest'
import { isPalindrome } from '../src/stringUtils'

describe('Pruebas de isPalindrome', () => {

  it('radar es palíndromo', () => {
    expect(isPalindrome("radar")).toBe(true)
  })

  it('anita lava la tina es palíndromo', () => {
    expect(isPalindrome("anita lava la tina")).toBe(true)
  })

  it('python no es palíndromo', () => {
    expect(isPalindrome("python")).toBe(false)
  })

  it('cadena vacía es palíndromo', () => {
    expect(isPalindrome("")).toBe(true)
  })

  it('Radar con mayúscula es palíndromo', () => {
    expect(isPalindrome("Radar")).toBe(true)
  })

})