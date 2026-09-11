class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,8,24] pre
        #[6,24,48,48] post

        
        n = len(nums)
        prefix_products = [nums[0]]

        for i in range(1,len(nums)):
            prefix_products.append(prefix_products[i-1]*nums[i])

        postfix_products = [nums[-1]]

        rev = nums[::-1]

        for i in range(1,len(rev)):
            postfix_products.append(postfix_products[i-1]*rev[i])

        postfix_products = postfix_products[::-1]

        ans = []

        for i in range(len(nums)):
            left_product = prefix_products[i-1] if i > 0 else 1
            
            # If i is the last index, there is nothing to the right, so default to 1
            right_product = postfix_products[i+1] if i < len(nums) - 1 else 1
            ans.append(left_product * right_product)
        return ans
            

        