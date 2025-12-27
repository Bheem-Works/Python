class Cat {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  catName(){
    // I for how to i call the element over here; 
    let version = 4.001; 
    return this.name + "is a cat"+ 'version' + version ; 
  }
}

const call_cat = new Cat('micchi','2 months');
console.log(call_cat.catName());
console.log(call_cat);


// Quick functions; 
(
  ()=>{
    console.log("hello my name is miso");
  }
)();