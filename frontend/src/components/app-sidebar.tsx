import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarHeader,
  SidebarGroupContent, SidebarGroupLabel, SidebarMenu, SidebarMenuButton, SidebarMenuItem,
} from "@/components/ui/sidebar"
import { NavLink } from "react-router"
import { ModeToggle } from "./mode-toggle"

export function AppSidebar() {
  const data = {
    navMain: [
      {
        title: "Main",
        url: "#",
        items: [
          {
            title: "Dashboard",
            url: "dashboard",
          },
        ],
      },
    ],
  }

  return (
    <Sidebar>
      <SidebarHeader>Finance App</SidebarHeader>
      <SidebarContent>
        {data.navMain.map((item) =>
          <SidebarGroup>
            <SidebarGroupLabel>{item.title}</SidebarGroupLabel>
            <SidebarGroupContent>
              <SidebarMenu>
                {item.items.map((item) =>
                  <SidebarMenuItem>
                    <SidebarMenuButton>
                      <NavLink to={item.url}>{item.title}</NavLink>
                    </SidebarMenuButton>
                  </SidebarMenuItem>
                )}
              </SidebarMenu>
            </SidebarGroupContent>
          </SidebarGroup>
        )}
      </SidebarContent>
      <SidebarFooter>
        <ModeToggle />
      </SidebarFooter>
    </Sidebar >
  )
}
