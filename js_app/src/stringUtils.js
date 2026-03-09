/**
 * Devuelve true si text es palíndromo (ignora espacios y mayúsculas/minúsculas).
 */
function isPalindrome(text) {
  const cleaned = text.toLowerCase().replace(/\s+/g, '');
  return cleaned === cleaned.split('').reverse().join('');
}

module.exports = { isPalindrome };
