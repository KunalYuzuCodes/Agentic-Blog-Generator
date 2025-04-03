<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/tools/">
      
      
        <link rel="prev" href="../agent/">
      
      
        <link rel="next" href="../common_tools/">
      
      
      <link rel="icon" href="../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_ai.tools - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_ai.tools - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/tools.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/tools/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_ai.tools - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/tools.png">
      
    
    
   <link href="../../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#pydantic_aitools" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href="../.." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../img/logo-white.svg" alt="logo">

    </a>
    <label class="md-header__button md-icon" for="__drawer">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"></path></svg>
    </label>
    <div class="md-header__title" data-md-component="header-title">
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            PydanticAI
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              pydantic_ai.tools
            
          </span>
        </div>
      </div>
    </div>
    
      
        <form class="md-header__option" data-md-component="palette">
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to light mode" type="radio" name="__palette" id="__palette_0">
    
      <label class="md-header__button md-icon" title="Switch to light mode" for="__palette_1">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 2.38 1.19 4.47 3 5.74V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.26c1.81-1.27 3-3.36 3-5.74a7 7 0 0 0-7-7M9 21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1H9z"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: light)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to dark mode" type="radio" name="__palette" id="__palette_1">
    
      <label class="md-header__button md-icon" title="Switch to dark mode" for="__palette_2" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7M9 21v-1h6v1a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1m3-17a5 5 0 0 0-5 5c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58a5 5 0 0 0-5-5"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: dark)" data-md-color-scheme="slate" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to system preference" type="radio" name="__palette" id="__palette_2">
    
      <label class="md-header__button md-icon" title="Switch to system preference" for="__palette_0" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 2c3.87 0 7 3.13 7 7 0 2.38-1.19 4.47-3 5.74V17c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1v-2.26C3.19 13.47 2 11.38 2 9c0-3.87 3.13-7 7-7M6 21v-1h6v1c0 .55-.45 1-1 1H7c-.55 0-1-.45-1-1M9 4C6.24 4 4 6.24 4 9c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58 0-2.76-2.24-5-5-5m10 9h-2l-3.2 9h1.9l.7-2h3.2l.7 2h1.9zm-2.15 5.65L18 15l1.15 3.65z"></path></svg>
      </label>
    
  
</form>
      
    
    
      <script>var palette=__md_get("__palette");if(palette&&palette.color){if("(prefers-color-scheme)"===palette.color.media){var media=matchMedia("(prefers-color-scheme: light)"),input=document.querySelector(media.matches?"[data-md-color-media='(prefers-color-scheme: light)']":"[data-md-color-media='(prefers-color-scheme: dark)']");palette.color.media=input.getAttribute("data-md-color-media"),palette.color.scheme=input.getAttribute("data-md-color-scheme"),palette.color.primary=input.getAttribute("data-md-color-primary"),palette.color.accent=input.getAttribute("data-md-color-accent")}for(var[key,value]of Object.entries(palette.color))document.body.setAttribute("data-md-color-"+key,value)}</script>
    
    
    
      <label class="md-header__button md-icon" for="__search">
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"></path></svg>
      </label>
      <div class="md-search" role="dialog">
  <label class="md-search__overlay" for="__search"></label>
  <div class="md-search__inner" role="search">
    <form class="md-search__form" name="search">
      <input type="text" id="searchbox" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" required="">
      <label class="md-search__icon md-icon" for="__search">

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.516 6.516 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5Z"></path></svg>

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 11v2H8l5.5 5.5-1.42 1.42L4.16 12l7.92-7.92L13.5 5.5 8 11h12Z"></path></svg>
      </label>
      <nav class="md-search__options" aria-label="Search">

        <button id="searchbox-clear" type="reset" class="md-search__icon md-icon" title="Clear" aria-label="Clear" tabindex="-1">

          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41Z"></path></svg>
        </button>
      </nav>

        <div class="md-search__suggest"></div>

    </form>
    <div class="md-search__output">
      <div class="md-search__scrollwrap" tabindex="0">
        <div class="md-search-result">
          <div class="md-search-result__meta" id="type-to-start-searching">Type to start searching</div>
          <ol class="md-search-result__list" id="hits" role="presentation" hidden=""></ol>
        </div>
      </div>
    </div>
  </div>
</div>
    
    
      <div class="md-header__source">
        <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
      </div>
    
  </nav>
  
</header>
    
    <div class="md-container" data-md-component="container">
      
      
        
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation">
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    



<nav class="md-nav md-nav--primary" aria-label="Navigation" data-md-level="0">
  <label class="md-nav__title" for="__drawer">
    <a href="../.." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../img/logo-white.svg" alt="logo">

    </a>
    PydanticAI
  </label>
  
    <div class="md-nav__source">
      <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
    </div>
  
  <ul class="md-nav__list">
    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../.." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../troubleshooting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Troubleshooting
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6">
        
          
          <label class="md-nav__link" for="__nav_6" id="__nav_6_label" tabindex="">
            
  
  <span class="md-ellipsis">
    Documentation
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            Documentation
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../mcp/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    MCP
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_6_14" id="__nav_6_14_label" tabindex="0">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_14_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6_14">
            <span class="md-nav__icon md-icon"></span>
            MCP
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../cli/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Command Line Interface (CLI)
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../examples/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_7" id="__nav_7_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            Examples
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8" checked="">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools" class="md-nav__link">
    <span class="md-ellipsis">
      tools
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.AgentDepsT" class="md-nav__link">
    <span class="md-ellipsis">
      AgentDepsT
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext" class="md-nav__link">
    <span class="md-ellipsis">
      RunContext
    </span>
  </a>
  
    <nav class="md-nav" aria-label="RunContext">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.deps" class="md-nav__link">
    <span class="md-ellipsis">
      deps
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.model" class="md-nav__link">
    <span class="md-ellipsis">
      model
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.usage" class="md-nav__link">
    <span class="md-ellipsis">
      usage
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.prompt" class="md-nav__link">
    <span class="md-ellipsis">
      prompt
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.messages" class="md-nav__link">
    <span class="md-ellipsis">
      messages
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.tool_name" class="md-nav__link">
    <span class="md-ellipsis">
      tool_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.retry" class="md-nav__link">
    <span class="md-ellipsis">
      retry
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.run_step" class="md-nav__link">
    <span class="md-ellipsis">
      run_step
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolParams" class="md-nav__link">
    <span class="md-ellipsis">
      ToolParams
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.SystemPromptFunc" class="md-nav__link">
    <span class="md-ellipsis">
      SystemPromptFunc
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolFuncContext" class="md-nav__link">
    <span class="md-ellipsis">
      ToolFuncContext
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolFuncPlain" class="md-nav__link">
    <span class="md-ellipsis">
      ToolFuncPlain
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolFuncEither" class="md-nav__link">
    <span class="md-ellipsis">
      ToolFuncEither
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolPrepareFunc" class="md-nav__link">
    <span class="md-ellipsis">
      ToolPrepareFunc
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.DocstringFormat" class="md-nav__link">
    <span class="md-ellipsis">
      DocstringFormat
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.Tool" class="md-nav__link">
    <span class="md-ellipsis">
      Tool
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Tool">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.Tool.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.Tool.prepare_tool_def" class="md-nav__link">
    <span class="md-ellipsis">
      prepare_tool_def
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.Tool.run" class="md-nav__link">
    <span class="md-ellipsis">
      run
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ObjectJsonSchema" class="md-nav__link">
    <span class="md-ellipsis">
      ObjectJsonSchema
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolDefinition" class="md-nav__link">
    <span class="md-ellipsis">
      ToolDefinition
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ToolDefinition">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolDefinition.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolDefinition.description" class="md-nav__link">
    <span class="md-ellipsis">
      description
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolDefinition.parameters_json_schema" class="md-nav__link">
    <span class="md-ellipsis">
      parameters_json_schema
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolDefinition.outer_typed_dict_key" class="md-nav__link">
    <span class="md-ellipsis">
      outer_typed_dict_key
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/generation/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.generation
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" style="top: 48px;">
                <div class="md-sidebar__scrollwrap" style="height: 474px;">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools" class="md-nav__link">
    <span class="md-ellipsis">
      tools
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.AgentDepsT" class="md-nav__link">
    <span class="md-ellipsis">
      AgentDepsT
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext" class="md-nav__link">
    <span class="md-ellipsis">
      RunContext
    </span>
  </a>
  
    <nav class="md-nav" aria-label="RunContext">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.deps" class="md-nav__link">
    <span class="md-ellipsis">
      deps
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.model" class="md-nav__link">
    <span class="md-ellipsis">
      model
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.usage" class="md-nav__link">
    <span class="md-ellipsis">
      usage
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.prompt" class="md-nav__link">
    <span class="md-ellipsis">
      prompt
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.messages" class="md-nav__link">
    <span class="md-ellipsis">
      messages
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.tool_call_id" class="md-nav__link">
    <span class="md-ellipsis">
      tool_call_id
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.tool_name" class="md-nav__link">
    <span class="md-ellipsis">
      tool_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.retry" class="md-nav__link">
    <span class="md-ellipsis">
      retry
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.RunContext.run_step" class="md-nav__link">
    <span class="md-ellipsis">
      run_step
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolParams" class="md-nav__link">
    <span class="md-ellipsis">
      ToolParams
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.SystemPromptFunc" class="md-nav__link">
    <span class="md-ellipsis">
      SystemPromptFunc
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolFuncContext" class="md-nav__link">
    <span class="md-ellipsis">
      ToolFuncContext
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolFuncPlain" class="md-nav__link">
    <span class="md-ellipsis">
      ToolFuncPlain
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolFuncEither" class="md-nav__link">
    <span class="md-ellipsis">
      ToolFuncEither
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolPrepareFunc" class="md-nav__link">
    <span class="md-ellipsis">
      ToolPrepareFunc
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.DocstringFormat" class="md-nav__link">
    <span class="md-ellipsis">
      DocstringFormat
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.Tool" class="md-nav__link">
    <span class="md-ellipsis">
      Tool
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Tool">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.Tool.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.Tool.prepare_tool_def" class="md-nav__link">
    <span class="md-ellipsis">
      prepare_tool_def
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.Tool.run" class="md-nav__link">
    <span class="md-ellipsis">
      run
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ObjectJsonSchema" class="md-nav__link">
    <span class="md-ellipsis">
      ObjectJsonSchema
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolDefinition" class="md-nav__link">
    <span class="md-ellipsis">
      ToolDefinition
    </span>
  </a>
  
    <nav class="md-nav" aria-label="ToolDefinition">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolDefinition.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolDefinition.description" class="md-nav__link">
    <span class="md-ellipsis">
      description
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolDefinition.parameters_json_schema" class="md-nav__link">
    <span class="md-ellipsis">
      parameters_json_schema
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.tools.ToolDefinition.outer_typed_dict_key" class="md-nav__link">
    <span class="md-ellipsis">
      outer_typed_dict_key
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


<h1 id="pydantic_aitools"><code>pydantic_ai.tools</code></h1>


<div class="doc doc-object doc-module">



<a id="pydantic_ai.tools"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">



































<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.tools.AgentDepsT" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">AgentDepsT</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="n">AgentDepsT</span> <span class="o">=</span> <span class="n"><span title="typing_extensions.TypeVar">TypeVar</span></span><span class="p">(</span>
    <span class="s2">"AgentDepsT"</span><span class="p">,</span> <span class="n"><span title="typing_extensions.TypeVar(default)">default</span></span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n"><span title="typing_extensions.TypeVar(contravariant)">contravariant</span></span><span class="o">=</span><span class="kc">True</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Type variable for agent dependencies.</p>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.tools.RunContext" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">RunContext</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>]</code></p>


        <p>Information about the current call.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/tools.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span></pre></div></td><td class="code"><div><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="nd">@dataclasses</span><span class="o">.</span><span class="n">dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">RunContext</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Information about the current call."""</span>

    <span class="n">deps</span><span class="p">:</span> <span class="n">AgentDepsT</span>
<span class="w">    </span><span class="sd">"""Dependencies for the agent."""</span>
    <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span>
<span class="w">    </span><span class="sd">"""The model used in this run."""</span>
    <span class="n">usage</span><span class="p">:</span> <span class="n">Usage</span>
<span class="w">    </span><span class="sd">"""LLM usage associated with the run."""</span>
    <span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">UserContent</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""The original user prompt passed to the run."""</span>
    <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""Messages exchanged in the conversation so far."""</span>
    <span class="n">tool_call_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The ID of the tool call."""</span>
    <span class="n">tool_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Name of the tool being called."""</span>
    <span class="n">retry</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
<span class="w">    </span><span class="sd">"""Number of retries so far."""</span>
    <span class="n">run_step</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
<span class="w">    </span><span class="sd">"""The current step in the run."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">replace_with</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">retry</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">tool_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">|</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]:</span>
        <span class="c1"># Create a new `RunContext` a new `retry` value and `tool_name`.</span>
        <span class="n">kwargs</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">if</span> <span class="n">retry</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s1">'retry'</span><span class="p">]</span> <span class="o">=</span> <span class="n">retry</span>
        <span class="k">if</span> <span class="n">tool_name</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span><span class="p">:</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s1">'tool_name'</span><span class="p">]</span> <span class="o">=</span> <span class="n">tool_name</span>
        <span class="k">return</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.RunContext.deps" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">deps</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Dependencies for the agent.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.RunContext.model" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">model</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="n">model</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.Model" href="../models/base/#pydantic_ai.models.Model">Model</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The model used in this run.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.RunContext.usage" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">usage</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="n">usage</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>LLM usage associated with the run.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.RunContext.prompt" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">prompt</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="n">prompt</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><span title="pydantic_ai.messages.UserContent">UserContent</span></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The original user prompt passed to the run.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.RunContext.messages" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">messages</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="n">messages</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="dataclasses.field" href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field">field</a></span><span class="p">(</span><span class="n"><span title="dataclasses.field(default_factory)">default_factory</span></span><span class="o">=</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Messages exchanged in the conversation so far.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.RunContext.tool_call_id" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_call_id</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="n">tool_call_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The ID of the tool call.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.RunContext.tool_name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">tool_name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="n">tool_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Name of the tool being called.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.RunContext.retry" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">retry</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code><span class="n">retry</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">=</span> <span class="mi">0</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Number of retries so far.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.RunContext.run_step" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">run_step</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="n">run_step</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">=</span> <span class="mi">0</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The current step in the run.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.tools.ToolParams" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ToolParams</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="n">ToolParams</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.ParamSpec" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.ParamSpec">ParamSpec</a></span><span class="p">(</span><span class="s1">'ToolParams'</span><span class="p">,</span> <span class="n"><span title="typing_extensions.ParamSpec(default)">default</span></span><span class="o">=...</span><span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Retrieval function param spec.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.tools.SystemPromptFunc" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">SystemPromptFunc</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="n">SystemPromptFunc</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]],</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]],</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[],</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[[],</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]],</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A function that may or maybe not take <code>RunContext</code> as an argument, and may or may not be async.</p>
<p>Usage <code>SystemPromptFunc[AgentDepsT]</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.tools.ToolFuncContext" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ToolFuncContext</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="n">ToolFuncContext</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.Concatenate" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Concatenate">Concatenate</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">],</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A tool function that takes <code>RunContext</code> as the first argument.</p>
<p>Usage <code>ToolContextFunc[AgentDepsT, ToolParams]</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.tools.ToolFuncPlain" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ToolFuncPlain</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="n">ToolFuncPlain</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Callable" href="https://docs.python.org/3/library/typing.html#typing.Callable">Callable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A tool function that does not take <code>RunContext</code> as the first argument.</p>
<p>Usage <code>ToolPlainFunc[ToolParams]</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.tools.ToolFuncEither" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ToolFuncEither</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="n">ToolFuncEither</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span>
    <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncContext" href="#pydantic_ai.tools.ToolFuncContext">ToolFuncContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">],</span>
    <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncPlain" href="#pydantic_ai.tools.ToolFuncPlain">ToolFuncPlain</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolParams" href="#pydantic_ai.tools.ToolParams">ToolParams</a></span><span class="p">],</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Either kind of tool function.</p>
<p>This is just a union of <a class="autorefs autorefs-internal" href="#pydantic_ai.tools.ToolFuncContext"><code>ToolFuncContext</code></a> and
<a class="autorefs autorefs-internal" href="#pydantic_ai.tools.ToolFuncPlain"><code>ToolFuncPlain</code></a>.</p>
<p>Usage <code>ToolFuncEither[AgentDepsT, ToolParams]</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.tools.ToolPrepareFunc" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ToolPrepareFunc</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code><span class="n">ToolPrepareFunc</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.TypeAlias" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeAlias">TypeAlias</a></span> <span class="o">=</span> <span class="p">(</span>
    <span class="s2">"Callable[[RunContext[AgentDepsT], ToolDefinition], Awaitable[ToolDefinition | None]]"</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Definition of a function that can prepare a tool definition at call time.</p>
<p>See <a href="../../tools/#tool-prepare">tool docs</a> for more information.</p>
<p>Example — here <code>only_if_42</code> is valid as a <code>ToolPrepareFunc</code>:</p>
<div class="language-python highlight"><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Union</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">RunContext</span><span class="p">,</span> <span class="n">Tool</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.tools</span><span class="w"> </span><span class="kn">import</span> <span class="n">ToolDefinition</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">only_if_42</span><span class="p">(</span>
    <span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">tool_def</span><span class="p">:</span> <span class="n">ToolDefinition</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">ToolDefinition</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
    <span class="k">if</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span> <span class="o">==</span> <span class="mi">42</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">tool_def</span>

<span class="k">def</span><span class="w"> </span><span class="nf">hitchhiker</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">answer</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="si">}</span><span class="s1"> </span><span class="si">{</span><span class="n">answer</span><span class="si">}</span><span class="s1">'</span>

<span class="n">hitchhiker</span> <span class="o">=</span> <span class="n">Tool</span><span class="p">(</span><span class="n">hitchhiker</span><span class="p">,</span> <span class="n">prepare</span><span class="o">=</span><span class="n">only_if_42</span><span class="p">)</span>
</code></pre></div>
<p>Usage <code>ToolPrepareFunc[AgentDepsT]</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.tools.DocstringFormat" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">DocstringFormat</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="n">DocstringFormat</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span>
    <span class="s2">"google"</span><span class="p">,</span> <span class="s2">"numpy"</span><span class="p">,</span> <span class="s2">"sphinx"</span><span class="p">,</span> <span class="s2">"auto"</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Supported docstring formats.</p>
<ul>
<li><code>'google'</code> — <a href="https://google.github.io/styleguide/pyguide.html#381-docstrings">Google-style</a> docstrings.</li>
<li><code>'numpy'</code> — <a href="https://numpydoc.readthedocs.io/en/latest/format.html">Numpy-style</a> docstrings.</li>
<li><code>'sphinx'</code> — <a href="https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html#the-sphinx-docstring-format">Sphinx-style</a> docstrings.</li>
<li><code>'auto'</code> — Automatically infer the format based on the structure of the docstring.</li>
</ul>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.tools.Tool" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">Tool</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>]</code></p>


        <p>A tool function for an agent.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/tools.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span>
<span class="normal">350</span>
<span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span>
<span class="normal">358</span>
<span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span>
<span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span>
<span class="normal">373</span>
<span class="normal">374</span>
<span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span></pre></div></td><td class="code"><div><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code tabindex="0"><span class="nd">@dataclass</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Tool</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""A tool function for an agent."""</span>

    <span class="n">function</span><span class="p">:</span> <span class="n">ToolFuncEither</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span>
    <span class="n">takes_ctx</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">max_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">description</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">prepare</span><span class="p">:</span> <span class="n">ToolPrepareFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">docstring_format</span><span class="p">:</span> <span class="n">DocstringFormat</span>
    <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">_is_async</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_single_arg_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_positional_fields</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_var_positional_field</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_validator</span><span class="p">:</span> <span class="n">SchemaValidator</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_parameters_json_schema</span><span class="p">:</span> <span class="n">ObjectJsonSchema</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="c1"># TODO: Move this state off the Tool class, which is otherwise stateless.</span>
    <span class="c1">#   This should be tracked inside a specific agent run, not the tool.</span>
    <span class="n">current_retry</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">function</span><span class="p">:</span> <span class="n">ToolFuncEither</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">takes_ctx</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">max_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">description</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">prepare</span><span class="p">:</span> <span class="n">ToolPrepareFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">docstring_format</span><span class="p">:</span> <span class="n">DocstringFormat</span> <span class="o">=</span> <span class="s1">'auto'</span><span class="p">,</span>
        <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
        <span class="n">schema_generator</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">GenerateJsonSchema</span><span class="p">]</span> <span class="o">=</span> <span class="n">GenerateToolJsonSchema</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Create a new tool instance.</span>

<span class="sd">        Example usage:</span>

<span class="sd">        ```python {noqa="I001"}</span>
<span class="sd">        from pydantic_ai import Agent, RunContext, Tool</span>

<span class="sd">        async def my_tool(ctx: RunContext[int], x: int, y: int) -&gt; str:</span>
<span class="sd">            return f'{ctx.deps} {x} {y}'</span>

<span class="sd">        agent = Agent('test', tools=[Tool(my_tool)])</span>
<span class="sd">        ```</span>

<span class="sd">        or with a custom prepare method:</span>

<span class="sd">        ```python {noqa="I001"}</span>
<span class="sd">        from typing import Union</span>

<span class="sd">        from pydantic_ai import Agent, RunContext, Tool</span>
<span class="sd">        from pydantic_ai.tools import ToolDefinition</span>

<span class="sd">        async def my_tool(ctx: RunContext[int], x: int, y: int) -&gt; str:</span>
<span class="sd">            return f'{ctx.deps} {x} {y}'</span>

<span class="sd">        async def prep_my_tool(</span>
<span class="sd">            ctx: RunContext[int], tool_def: ToolDefinition</span>
<span class="sd">        ) -&gt; Union[ToolDefinition, None]:</span>
<span class="sd">            # only register the tool if `deps == 42`</span>
<span class="sd">            if ctx.deps == 42:</span>
<span class="sd">                return tool_def</span>

<span class="sd">        agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])</span>
<span class="sd">        ```</span>


<span class="sd">        Args:</span>
<span class="sd">            function: The Python function to call as the tool.</span>
<span class="sd">            takes_ctx: Whether the function takes a [`RunContext`][pydantic_ai.tools.RunContext] first argument,</span>
<span class="sd">                this is inferred if unset.</span>
<span class="sd">            max_retries: Maximum number of retries allowed for this tool, set to the agent default if `None`.</span>
<span class="sd">            name: Name of the tool, inferred from the function if `None`.</span>
<span class="sd">            description: Description of the tool, inferred from the function if `None`.</span>
<span class="sd">            prepare: custom method to prepare the tool definition for each step, return `None` to omit this</span>
<span class="sd">                tool from a given step. This is useful if you want to customise a tool at call time,</span>
<span class="sd">                or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].</span>
<span class="sd">            docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].</span>
<span class="sd">                Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.</span>
<span class="sd">            require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.</span>
<span class="sd">            schema_generator: The JSON schema generator class to use. Defaults to `GenerateToolJsonSchema`.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">takes_ctx</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">takes_ctx</span> <span class="o">=</span> <span class="n">_pydantic</span><span class="o">.</span><span class="n">takes_ctx</span><span class="p">(</span><span class="n">function</span><span class="p">)</span>

        <span class="n">f</span> <span class="o">=</span> <span class="n">_pydantic</span><span class="o">.</span><span class="n">function_schema</span><span class="p">(</span>
            <span class="n">function</span><span class="p">,</span> <span class="n">takes_ctx</span><span class="p">,</span> <span class="n">docstring_format</span><span class="p">,</span> <span class="n">require_parameter_descriptions</span><span class="p">,</span> <span class="n">schema_generator</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">function</span> <span class="o">=</span> <span class="n">function</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">takes_ctx</span> <span class="o">=</span> <span class="n">takes_ctx</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span> <span class="o">=</span> <span class="n">max_retries</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span> <span class="ow">or</span> <span class="n">function</span><span class="o">.</span><span class="vm">__name__</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">description</span> <span class="o">=</span> <span class="n">description</span> <span class="ow">or</span> <span class="n">f</span><span class="p">[</span><span class="s1">'description'</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">prepare</span> <span class="o">=</span> <span class="n">prepare</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">docstring_format</span> <span class="o">=</span> <span class="n">docstring_format</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">require_parameter_descriptions</span> <span class="o">=</span> <span class="n">require_parameter_descriptions</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_is_async</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">iscoroutinefunction</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">function</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_single_arg_name</span> <span class="o">=</span> <span class="n">f</span><span class="p">[</span><span class="s1">'single_arg_name'</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_positional_fields</span> <span class="o">=</span> <span class="n">f</span><span class="p">[</span><span class="s1">'positional_fields'</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_var_positional_field</span> <span class="o">=</span> <span class="n">f</span><span class="p">[</span><span class="s1">'var_positional_field'</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_validator</span> <span class="o">=</span> <span class="n">f</span><span class="p">[</span><span class="s1">'validator'</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_parameters_json_schema</span> <span class="o">=</span> <span class="n">f</span><span class="p">[</span><span class="s1">'json_schema'</span><span class="p">]</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">prepare_tool_def</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ToolDefinition</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the tool definition.</span>

<span class="sd">        By default, this method creates a tool definition, then either returns it, or calls `self.prepare`</span>
<span class="sd">        if it's set.</span>

<span class="sd">        Returns:</span>
<span class="sd">            return a `ToolDefinition` or `None` if the tools should not be registered for this run.</span>
<span class="sd">        """</span>
        <span class="n">tool_def</span> <span class="o">=</span> <span class="n">ToolDefinition</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="n">description</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">description</span><span class="p">,</span>
            <span class="n">parameters_json_schema</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_parameters_json_schema</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">prepare</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">prepare</span><span class="p">(</span><span class="n">ctx</span><span class="p">,</span> <span class="n">tool_def</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">tool_def</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolCallPart</span><span class="p">,</span> <span class="n">run_context</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">],</span> <span class="n">tracer</span><span class="p">:</span> <span class="n">Tracer</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolReturnPart</span> <span class="o">|</span> <span class="n">_messages</span><span class="o">.</span><span class="n">RetryPromptPart</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the tool function asynchronously.</span>

<span class="sd">        This method wraps `_run` in an OpenTelemetry span.</span>

<span class="sd">        See &lt;https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/#execute-tool-span&gt;.</span>
<span class="sd">        """</span>
        <span class="n">span_attributes</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s1">'gen_ai.tool.name'</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
            <span class="c1"># NOTE: this means `gen_ai.tool.call.id` will be included even if it was generated by pydantic-ai</span>
            <span class="s1">'gen_ai.tool.call.id'</span><span class="p">:</span> <span class="n">message</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
            <span class="s1">'tool_arguments'</span><span class="p">:</span> <span class="n">message</span><span class="o">.</span><span class="n">args_as_json_str</span><span class="p">(),</span>
            <span class="s1">'logfire.msg'</span><span class="p">:</span> <span class="sa">f</span><span class="s1">'running tool: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span>
            <span class="c1"># add the JSON schema so these attributes are formatted nicely in Logfire</span>
            <span class="s1">'logfire.json_schema'</span><span class="p">:</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span>
                <span class="p">{</span>
                    <span class="s1">'type'</span><span class="p">:</span> <span class="s1">'object'</span><span class="p">,</span>
                    <span class="s1">'properties'</span><span class="p">:</span> <span class="p">{</span>
                        <span class="s1">'tool_arguments'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'type'</span><span class="p">:</span> <span class="s1">'object'</span><span class="p">},</span>
                        <span class="s1">'gen_ai.tool.name'</span><span class="p">:</span> <span class="p">{},</span>
                        <span class="s1">'gen_ai.tool.call.id'</span><span class="p">:</span> <span class="p">{},</span>
                    <span class="p">},</span>
                <span class="p">}</span>
            <span class="p">),</span>
        <span class="p">}</span>
        <span class="k">with</span> <span class="n">tracer</span><span class="o">.</span><span class="n">start_as_current_span</span><span class="p">(</span><span class="s1">'running tool'</span><span class="p">,</span> <span class="n">attributes</span><span class="o">=</span><span class="n">span_attributes</span><span class="p">):</span>
            <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="p">(</span><span class="n">message</span><span class="p">,</span> <span class="n">run_context</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_run</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolCallPart</span><span class="p">,</span> <span class="n">run_context</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolReturnPart</span> <span class="o">|</span> <span class="n">_messages</span><span class="o">.</span><span class="n">RetryPromptPart</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">message</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
                <span class="n">args_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validator</span><span class="o">.</span><span class="n">validate_json</span><span class="p">(</span><span class="n">message</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">args_dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validator</span><span class="o">.</span><span class="n">validate_python</span><span class="p">(</span><span class="n">message</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">ValidationError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_error</span><span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

        <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_call_args</span><span class="p">(</span><span class="n">args_dict</span><span class="p">,</span> <span class="n">message</span><span class="p">,</span> <span class="n">run_context</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_async</span><span class="p">:</span>
                <span class="n">function</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Callable</span><span class="p">[[</span><span class="n">Any</span><span class="p">],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="nb">str</span><span class="p">]],</span> <span class="bp">self</span><span class="o">.</span><span class="n">function</span><span class="p">)</span>
                <span class="n">response_content</span> <span class="o">=</span> <span class="k">await</span> <span class="n">function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">function</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">Callable</span><span class="p">[[</span><span class="n">Any</span><span class="p">],</span> <span class="nb">str</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">function</span><span class="p">)</span>
                <span class="n">response_content</span> <span class="o">=</span> <span class="k">await</span> <span class="n">_utils</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="n">function</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
        <span class="k">except</span> <span class="n">ModelRetry</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_error</span><span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="n">message</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">current_retry</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">return</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolReturnPart</span><span class="p">(</span>
            <span class="n">tool_name</span><span class="o">=</span><span class="n">message</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span>
            <span class="n">content</span><span class="o">=</span><span class="n">response_content</span><span class="p">,</span>
            <span class="n">tool_call_id</span><span class="o">=</span><span class="n">message</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_call_args</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">args_dict</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
        <span class="n">message</span><span class="p">:</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolCallPart</span><span class="p">,</span>
        <span class="n">run_context</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_single_arg_name</span><span class="p">:</span>
            <span class="n">args_dict</span> <span class="o">=</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_single_arg_name</span><span class="p">:</span> <span class="n">args_dict</span><span class="p">}</span>

        <span class="n">ctx</span> <span class="o">=</span> <span class="n">dataclasses</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span>
            <span class="n">run_context</span><span class="p">,</span>
            <span class="n">retry</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">current_retry</span><span class="p">,</span>
            <span class="n">tool_name</span><span class="o">=</span><span class="n">message</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span>
            <span class="n">tool_call_id</span><span class="o">=</span><span class="n">message</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">args</span> <span class="o">=</span> <span class="p">[</span><span class="n">ctx</span><span class="p">]</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">takes_ctx</span> <span class="k">else</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">positional_field</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_positional_fields</span><span class="p">:</span>
            <span class="n">args</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">args_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">positional_field</span><span class="p">))</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_var_positional_field</span><span class="p">:</span>
            <span class="n">args</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">args_dict</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_var_positional_field</span><span class="p">))</span>

        <span class="k">return</span> <span class="n">args</span><span class="p">,</span> <span class="n">args_dict</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_on_error</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">exc</span><span class="p">:</span> <span class="n">ValidationError</span> <span class="o">|</span> <span class="n">ModelRetry</span><span class="p">,</span> <span class="n">call_message</span><span class="p">:</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolCallPart</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_messages</span><span class="o">.</span><span class="n">RetryPromptPart</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">current_retry</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_retry</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">UnexpectedModelBehavior</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Tool exceeded max retries count of </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span> <span class="kn">from</span><span class="w"> </span><span class="nn">exc</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">exc</span><span class="p">,</span> <span class="n">ValidationError</span><span class="p">):</span>
                <span class="n">content</span> <span class="o">=</span> <span class="n">exc</span><span class="o">.</span><span class="n">errors</span><span class="p">(</span><span class="n">include_url</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">content</span> <span class="o">=</span> <span class="n">exc</span><span class="o">.</span><span class="n">message</span>
            <span class="k">return</span> <span class="n">_messages</span><span class="o">.</span><span class="n">RetryPromptPart</span><span class="p">(</span>
                <span class="n">tool_name</span><span class="o">=</span><span class="n">call_message</span><span class="o">.</span><span class="n">tool_name</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="n">content</span><span class="p">,</span>
                <span class="n">tool_call_id</span><span class="o">=</span><span class="n">call_message</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
            <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.tools.Tool.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="nf">function</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncEither" href="#pydantic_ai.tools.ToolFuncEither">ToolFuncEither</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">takes_ctx</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">max_retries</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">description</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prepare</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolPrepareFunc" href="#pydantic_ai.tools.ToolPrepareFunc">ToolPrepareFunc</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">docstring_format</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.DocstringFormat" href="#pydantic_ai.tools.DocstringFormat">DocstringFormat</a></span> <span class="o">=</span> <span class="s2">"auto"</span><span class="p">,</span>
    <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">schema_generator</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span>
        <span class="n"><a class="autorefs autorefs-external" title="pydantic.json_schema.GenerateJsonSchema" href="https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema">GenerateJsonSchema</a></span>
    <span class="p">]</span> <span class="o">=</span> <span class="n"><span title="pydantic_ai.tools.GenerateToolJsonSchema">GenerateToolJsonSchema</span></span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a new tool instance.</p>
<p>Example usage:</p>
<div class="language-python highlight"><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">RunContext</span><span class="p">,</span> <span class="n">Tool</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">my_tool</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">x</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="si">}</span><span class="s1"> </span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s1"> </span><span class="si">{</span><span class="n">y</span><span class="si">}</span><span class="s1">'</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'test'</span><span class="p">,</span> <span class="n">tools</span><span class="o">=</span><span class="p">[</span><span class="n">Tool</span><span class="p">(</span><span class="n">my_tool</span><span class="p">)])</span>
</code></pre></div>
<p>or with a custom prepare method:</p>
<div class="language-python highlight"><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Union</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">RunContext</span><span class="p">,</span> <span class="n">Tool</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.tools</span><span class="w"> </span><span class="kn">import</span> <span class="n">ToolDefinition</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">my_tool</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">x</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">return</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="si">}</span><span class="s1"> </span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s1"> </span><span class="si">{</span><span class="n">y</span><span class="si">}</span><span class="s1">'</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">prep_my_tool</span><span class="p">(</span>
    <span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">tool_def</span><span class="p">:</span> <span class="n">ToolDefinition</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Union</span><span class="p">[</span><span class="n">ToolDefinition</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
    <span class="c1"># only register the tool if `deps == 42`</span>
    <span class="k">if</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span> <span class="o">==</span> <span class="mi">42</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">tool_def</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'test'</span><span class="p">,</span> <span class="n">tools</span><span class="o">=</span><span class="p">[</span><span class="n">Tool</span><span class="p">(</span><span class="n">my_tool</span><span class="p">,</span> <span class="n">prepare</span><span class="o">=</span><span class="n">prep_my_tool</span><span class="p">)])</span>
</code></pre></div>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>function</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolFuncEither" href="#pydantic_ai.tools.ToolFuncEither">ToolFuncEither</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The Python function to call as the tool.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>takes_ctx</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether the function takes a <a class="autorefs autorefs-internal" href="#pydantic_ai.tools.RunContext"><code>RunContext</code></a> first argument,
this is inferred if unset.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>max_retries</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Maximum number of retries allowed for this tool, set to the agent default if <code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Name of the tool, inferred from the function if <code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>description</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Description of the tool, inferred from the function if <code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>prepare</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolPrepareFunc" href="#pydantic_ai.tools.ToolPrepareFunc">ToolPrepareFunc</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>custom method to prepare the tool definition for each step, return <code>None</code> to omit this
tool from a given step. This is useful if you want to customise a tool at call time,
or omit it completely from a step. See <a class="autorefs autorefs-internal" href="#pydantic_ai.tools.ToolPrepareFunc"><code>ToolPrepareFunc</code></a>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>docstring_format</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.DocstringFormat" href="#pydantic_ai.tools.DocstringFormat">DocstringFormat</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The format of the docstring, see <a class="autorefs autorefs-internal" href="#pydantic_ai.tools.DocstringFormat"><code>DocstringFormat</code></a>.
Defaults to <code>'auto'</code>, such that the format is inferred from the structure of the docstring.</p>
              </div>
            </td>
            <td>
                  <code>'auto'</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>require_parameter_descriptions</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If True, raise an error if a parameter description is missing. Defaults to False.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>schema_generator</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-external" title="pydantic.json_schema.GenerateJsonSchema" href="https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema">GenerateJsonSchema</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The JSON schema generator class to use. Defaults to <code>GenerateToolJsonSchema</code>.</p>
              </div>
            </td>
            <td>
                  <code><span title="pydantic_ai.tools.GenerateToolJsonSchema">GenerateToolJsonSchema</span></code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/tools.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span></pre></div></td><td class="code"><div><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">function</span><span class="p">:</span> <span class="n">ToolFuncEither</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">takes_ctx</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">max_retries</span><span class="p">:</span> <span class="nb">int</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">description</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">prepare</span><span class="p">:</span> <span class="n">ToolPrepareFunc</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">docstring_format</span><span class="p">:</span> <span class="n">DocstringFormat</span> <span class="o">=</span> <span class="s1">'auto'</span><span class="p">,</span>
    <span class="n">require_parameter_descriptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
    <span class="n">schema_generator</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">GenerateJsonSchema</span><span class="p">]</span> <span class="o">=</span> <span class="n">GenerateToolJsonSchema</span><span class="p">,</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Create a new tool instance.</span>

<span class="sd">    Example usage:</span>

<span class="sd">    ```python {noqa="I001"}</span>
<span class="sd">    from pydantic_ai import Agent, RunContext, Tool</span>

<span class="sd">    async def my_tool(ctx: RunContext[int], x: int, y: int) -&gt; str:</span>
<span class="sd">        return f'{ctx.deps} {x} {y}'</span>

<span class="sd">    agent = Agent('test', tools=[Tool(my_tool)])</span>
<span class="sd">    ```</span>

<span class="sd">    or with a custom prepare method:</span>

<span class="sd">    ```python {noqa="I001"}</span>
<span class="sd">    from typing import Union</span>

<span class="sd">    from pydantic_ai import Agent, RunContext, Tool</span>
<span class="sd">    from pydantic_ai.tools import ToolDefinition</span>

<span class="sd">    async def my_tool(ctx: RunContext[int], x: int, y: int) -&gt; str:</span>
<span class="sd">        return f'{ctx.deps} {x} {y}'</span>

<span class="sd">    async def prep_my_tool(</span>
<span class="sd">        ctx: RunContext[int], tool_def: ToolDefinition</span>
<span class="sd">    ) -&gt; Union[ToolDefinition, None]:</span>
<span class="sd">        # only register the tool if `deps == 42`</span>
<span class="sd">        if ctx.deps == 42:</span>
<span class="sd">            return tool_def</span>

<span class="sd">    agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])</span>
<span class="sd">    ```</span>


<span class="sd">    Args:</span>
<span class="sd">        function: The Python function to call as the tool.</span>
<span class="sd">        takes_ctx: Whether the function takes a [`RunContext`][pydantic_ai.tools.RunContext] first argument,</span>
<span class="sd">            this is inferred if unset.</span>
<span class="sd">        max_retries: Maximum number of retries allowed for this tool, set to the agent default if `None`.</span>
<span class="sd">        name: Name of the tool, inferred from the function if `None`.</span>
<span class="sd">        description: Description of the tool, inferred from the function if `None`.</span>
<span class="sd">        prepare: custom method to prepare the tool definition for each step, return `None` to omit this</span>
<span class="sd">            tool from a given step. This is useful if you want to customise a tool at call time,</span>
<span class="sd">            or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].</span>
<span class="sd">        docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].</span>
<span class="sd">            Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.</span>
<span class="sd">        require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.</span>
<span class="sd">        schema_generator: The JSON schema generator class to use. Defaults to `GenerateToolJsonSchema`.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">takes_ctx</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">takes_ctx</span> <span class="o">=</span> <span class="n">_pydantic</span><span class="o">.</span><span class="n">takes_ctx</span><span class="p">(</span><span class="n">function</span><span class="p">)</span>

    <span class="n">f</span> <span class="o">=</span> <span class="n">_pydantic</span><span class="o">.</span><span class="n">function_schema</span><span class="p">(</span>
        <span class="n">function</span><span class="p">,</span> <span class="n">takes_ctx</span><span class="p">,</span> <span class="n">docstring_format</span><span class="p">,</span> <span class="n">require_parameter_descriptions</span><span class="p">,</span> <span class="n">schema_generator</span>
    <span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">function</span> <span class="o">=</span> <span class="n">function</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">takes_ctx</span> <span class="o">=</span> <span class="n">takes_ctx</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">max_retries</span> <span class="o">=</span> <span class="n">max_retries</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span> <span class="ow">or</span> <span class="n">function</span><span class="o">.</span><span class="vm">__name__</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">description</span> <span class="o">=</span> <span class="n">description</span> <span class="ow">or</span> <span class="n">f</span><span class="p">[</span><span class="s1">'description'</span><span class="p">]</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">prepare</span> <span class="o">=</span> <span class="n">prepare</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">docstring_format</span> <span class="o">=</span> <span class="n">docstring_format</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">require_parameter_descriptions</span> <span class="o">=</span> <span class="n">require_parameter_descriptions</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_is_async</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">iscoroutinefunction</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">function</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_single_arg_name</span> <span class="o">=</span> <span class="n">f</span><span class="p">[</span><span class="s1">'single_arg_name'</span><span class="p">]</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_positional_fields</span> <span class="o">=</span> <span class="n">f</span><span class="p">[</span><span class="s1">'positional_fields'</span><span class="p">]</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_var_positional_field</span> <span class="o">=</span> <span class="n">f</span><span class="p">[</span><span class="s1">'var_positional_field'</span><span class="p">]</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_validator</span> <span class="o">=</span> <span class="n">f</span><span class="p">[</span><span class="s1">'validator'</span><span class="p">]</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_parameters_json_schema</span> <span class="o">=</span> <span class="n">f</span><span class="p">[</span><span class="s1">'json_schema'</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.tools.Tool.prepare_tool_def" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">prepare_tool_def</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code><span class="nf">prepare_tool_def</span><span class="p">(</span>
    <span class="n">ctx</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolDefinition" href="#pydantic_ai.tools.ToolDefinition">ToolDefinition</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the tool definition.</p>
<p>By default, this method creates a tool definition, then either returns it, or calls <code>self.prepare</code>
if it's set.</p>


    <p><span class="doc-section-title">Returns:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ToolDefinition" href="#pydantic_ai.tools.ToolDefinition">ToolDefinition</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>return a <code>ToolDefinition</code> or <code>None</code> if the tools should not be registered for this run.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/tools.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span></pre></div></td><td class="code"><div><pre id="__code_25"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_25 > code"></button><code><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">prepare_tool_def</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">ToolDefinition</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get the tool definition.</span>

<span class="sd">    By default, this method creates a tool definition, then either returns it, or calls `self.prepare`</span>
<span class="sd">    if it's set.</span>

<span class="sd">    Returns:</span>
<span class="sd">        return a `ToolDefinition` or `None` if the tools should not be registered for this run.</span>
<span class="sd">    """</span>
    <span class="n">tool_def</span> <span class="o">=</span> <span class="n">ToolDefinition</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
        <span class="n">description</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">description</span><span class="p">,</span>
        <span class="n">parameters_json_schema</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_parameters_json_schema</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">prepare</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">prepare</span><span class="p">(</span><span class="n">ctx</span><span class="p">,</span> <span class="n">tool_def</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">tool_def</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.tools.Tool.run" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">run</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code><span class="nf">run</span><span class="p">(</span>
    <span class="n">message</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolCallPart" href="../messages/#pydantic_ai.messages.ToolCallPart">ToolCallPart</a></span><span class="p">,</span>
    <span class="n">run_context</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.RunContext" href="#pydantic_ai.tools.RunContext">RunContext</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="#pydantic_ai.tools.AgentDepsT">AgentDepsT</a></span><span class="p">],</span>
    <span class="n">tracer</span><span class="p">:</span> <span class="n"><span title="opentelemetry.trace.Tracer">Tracer</span></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ToolReturnPart" href="../messages/#pydantic_ai.messages.ToolReturnPart">ToolReturnPart</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.RetryPromptPart" href="../messages/#pydantic_ai.messages.RetryPromptPart">RetryPromptPart</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Run the tool function asynchronously.</p>
<p>This method wraps <code>_run</code> in an OpenTelemetry span.</p>
<p>See <a href="https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/#execute-tool-span">https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/#execute-tool-span</a>.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/tools.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span>
<span class="normal">299</span>
<span class="normal">300</span>
<span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span></pre></div></td><td class="code"><div><pre id="__code_27"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_27 > code"></button><code><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolCallPart</span><span class="p">,</span> <span class="n">run_context</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">],</span> <span class="n">tracer</span><span class="p">:</span> <span class="n">Tracer</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ToolReturnPart</span> <span class="o">|</span> <span class="n">_messages</span><span class="o">.</span><span class="n">RetryPromptPart</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the tool function asynchronously.</span>

<span class="sd">    This method wraps `_run` in an OpenTelemetry span.</span>

<span class="sd">    See &lt;https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/#execute-tool-span&gt;.</span>
<span class="sd">    """</span>
    <span class="n">span_attributes</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s1">'gen_ai.tool.name'</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
        <span class="c1"># NOTE: this means `gen_ai.tool.call.id` will be included even if it was generated by pydantic-ai</span>
        <span class="s1">'gen_ai.tool.call.id'</span><span class="p">:</span> <span class="n">message</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">,</span>
        <span class="s1">'tool_arguments'</span><span class="p">:</span> <span class="n">message</span><span class="o">.</span><span class="n">args_as_json_str</span><span class="p">(),</span>
        <span class="s1">'logfire.msg'</span><span class="p">:</span> <span class="sa">f</span><span class="s1">'running tool: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span>
        <span class="c1"># add the JSON schema so these attributes are formatted nicely in Logfire</span>
        <span class="s1">'logfire.json_schema'</span><span class="p">:</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span>
            <span class="p">{</span>
                <span class="s1">'type'</span><span class="p">:</span> <span class="s1">'object'</span><span class="p">,</span>
                <span class="s1">'properties'</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s1">'tool_arguments'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'type'</span><span class="p">:</span> <span class="s1">'object'</span><span class="p">},</span>
                    <span class="s1">'gen_ai.tool.name'</span><span class="p">:</span> <span class="p">{},</span>
                    <span class="s1">'gen_ai.tool.call.id'</span><span class="p">:</span> <span class="p">{},</span>
                <span class="p">},</span>
            <span class="p">}</span>
        <span class="p">),</span>
    <span class="p">}</span>
    <span class="k">with</span> <span class="n">tracer</span><span class="o">.</span><span class="n">start_as_current_span</span><span class="p">(</span><span class="s1">'running tool'</span><span class="p">,</span> <span class="n">attributes</span><span class="o">=</span><span class="n">span_attributes</span><span class="p">):</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run</span><span class="p">(</span><span class="n">message</span><span class="p">,</span> <span class="n">run_context</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.tools.ObjectJsonSchema" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ObjectJsonSchema</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_28"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_28 > code"></button><code><span class="n">ObjectJsonSchema</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.TypeAlias" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeAlias">TypeAlias</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Type representing JSON schema of an object, e.g. where <code>"type": "object"</code>.</p>
<p>This type is used to define tools parameters (aka arguments) in <a class="autorefs autorefs-internal" href="#pydantic_ai.tools.ToolDefinition">ToolDefinition</a>.</p>
<p>With PEP-728 this should be a TypedDict with <code>type: Literal['object']</code>, and <code>extra_parts=Any</code></p>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.tools.ToolDefinition" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">ToolDefinition</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>Definition of a tool passed to a model.</p>
<p>This is used for both function tools result tools.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/tools.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">399</span>
<span class="normal">400</span>
<span class="normal">401</span>
<span class="normal">402</span>
<span class="normal">403</span>
<span class="normal">404</span>
<span class="normal">405</span>
<span class="normal">406</span>
<span class="normal">407</span>
<span class="normal">408</span>
<span class="normal">409</span>
<span class="normal">410</span>
<span class="normal">411</span>
<span class="normal">412</span>
<span class="normal">413</span>
<span class="normal">414</span>
<span class="normal">415</span>
<span class="normal">416</span>
<span class="normal">417</span>
<span class="normal">418</span>
<span class="normal">419</span></pre></div></td><td class="code"><div><pre id="__code_29"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_29 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">ToolDefinition</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Definition of a tool passed to a model.</span>

<span class="sd">    This is used for both function tools result tools.</span>
<span class="sd">    """</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The name of the tool."""</span>

    <span class="n">description</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The description of the tool."""</span>

    <span class="n">parameters_json_schema</span><span class="p">:</span> <span class="n">ObjectJsonSchema</span>
<span class="w">    </span><span class="sd">"""The JSON schema for the tool's parameters."""</span>

    <span class="n">outer_typed_dict_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The key in the outer [TypedDict] that wraps a result tool.</span>

<span class="sd">    This will only be set for result tools which don't have an `object` JSON schema.</span>
<span class="sd">    """</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.ToolDefinition.name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_30"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_30 > code"></button><code><span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The name of the tool.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.ToolDefinition.description" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">description</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_31"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_31 > code"></button><code><span class="n">description</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The description of the tool.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.ToolDefinition.parameters_json_schema" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">parameters_json_schema</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_32"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_32 > code"></button><code><span class="n">parameters_json_schema</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.tools.ObjectJsonSchema" href="#pydantic_ai.tools.ObjectJsonSchema">ObjectJsonSchema</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The JSON schema for the tool's parameters.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.tools.ToolDefinition.outer_typed_dict_key" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">outer_typed_dict_key</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_33"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_33 > code"></button><code><span class="n">outer_typed_dict_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The key in the outer [TypedDict] that wraps a result tool.</p>
<p>This will only be set for result tools which don't have an <code>object</code> JSON schema.</p>
    </div>

</div>




  </div>

    </div>

</div>




  </div>

    </div>

</div>







  
  






                
              </article>
            </div>
          
          
  <script>var tabs=__md_get("__tabs");if(Array.isArray(tabs))e:for(var set of document.querySelectorAll(".tabbed-set")){var labels=set.querySelector(".tabbed-labels");for(var tab of tabs)for(var label of labels.getElementsByTagName("label"))if(label.innerText.trim()===tab){var input=document.getElementById(label.htmlFor);input.checked=!0;continue e}}</script>

<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
        </div>
        
      </main>
      
        <footer class="md-footer">
  
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">
  
    <div class="md-copyright__highlight">
      © Pydantic Services Inc. 2024 to present
    </div>
  
  
</div>
      
    </div>
  </div>
</footer>
      
    </div>
    <div class="md-dialog" data-md-component="dialog">
      <div class="md-dialog__inner md-typeset"></div>
    </div>
    
    
    <script id="__config" type="application/json">{"base": "../..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>