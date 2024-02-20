```mermaid
C4Context

title Sales Domain Bounded Countext Diagram

Enterprise_Boundary(snm, "Sales & Marketing") {

    Deployment_Node(customer, "Customer") {
        Person(cust, "Customer")
    }

    Deployment_Node(marketing, "Marketing") {
        Component(campaign, "Campaign")
    }

    Deployment_Node(sales, "Sales") {
        Person(sales_rep, "Sales Representative")
        Person(sales_manager, "Sales Manager")

        Deployment_Node(tsd, "Territory Subdomain") {
            
            Component(terr, "Territory")
            Component(area, "Area")
            Component(region, "Region")            
        }
        
    }

}

Rel(cust, terr, "Within")
Rel(terr, area, "Contains")
Rel(area, region, "Contains")
Rel(sales_rep, terr, "Owns")
Rel(sales_manager, sales_rep, "Supervises")
Rel(sales_manager, area, "Owns")
Rel(sales_manager, region, "Owns")

UpdateRelStyle(sales_rep, terr, $offsetY="-40", $offsetX="40")
UpdateRelStyle(sales_manager, $offsetY="40", $offsetX="4")
UpdateRelStyle(sales_manager, $offsetY="40", $offsetX="4")
UpdateRelStyle(sales_manager, $offsetY="40", $offsetX="4")
```