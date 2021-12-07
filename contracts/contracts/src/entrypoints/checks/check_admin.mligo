// Function that checks if an account is admin
// Must be integrated into functions that can only be used by admin 
let is_admin(u, s: address * marketplace_storage) : bool =
        u = s.admin
