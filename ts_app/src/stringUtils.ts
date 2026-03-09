/**
 * Devuelve true si text es palíndromo (ignora espacios y mayúsculas/minúsculas).
 */
export function isPalindrome(text: string): boolean {
  const cleaned = text.toLowerCase().replace(/\s+/g, '');
  return cleaned === cleaned.split('').reverse().join('');
}
