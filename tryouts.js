arr = ['Mexico','USA','Israel']
filter = 'I'

console.log(arr.filter(country => {
  country.toLowerCase().indexOf(filter.toLowerCase()) > 0)
})