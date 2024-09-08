export default async () => {
  const response = await fetch('http://127.0.0.1:3451/api/')
  const textResponse = await response.text()
  return textResponse
}