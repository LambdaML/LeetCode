package easy

/**
  * Created by Administrator on 2018/9/4.
  */
object No152_Maximum_Product_Subarray {
  /**
    * 连续的多个负值也可以相成，那么就必须将所有可能都遍历一下，简单的判断是不可行的
    * @param nums
    * @return
    */
  def maxProduct1(nums: Array[Int]): Int = {
    var max_product=nums.head
    for(i<-nums.indices){
      var index=i+1
      while(nums.slice(i,index).product>=max_product && index<=nums.length+1) {
        max_product=nums.slice(i,index).product
        index+=1
      }
    }
    max_product
  }


  def maxProduct(nums: Array[Int]): Int = {
    var max_product=nums.head
    for(i<-nums.indices){
        nums.drop(i).inits.toArray.dropRight(1).foreach(arr=>{
  val current_product=arr.product
  if(current_product>max_product) max_product=current_product
})

    }
    max_product
  }

  def main(args: Array[String]): Unit = {
//val arr=Array(2,3,-2,4)
//val arr=Array(-2,0,-1)
val arr=Array(0,2)
    println(maxProduct(arr))
  }
}
