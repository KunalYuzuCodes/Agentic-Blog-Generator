<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/result/">
      
      
        <link rel="prev" href="../common_tools/">
      
      
        <link rel="next" href="../messages/">
      
      
      <link rel="icon" href="../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_ai.result - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_ai.result - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/result.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/result/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_ai.result - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/result.png">
      
    
    
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
      
        
        <a href="#pydantic_airesult" class="md-skip">
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
            
              pydantic_ai.result
            
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
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.result" class="md-nav__link">
    <span class="md-ellipsis">
      result
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.result.ResultDataT" class="md-nav__link">
    <span class="md-ellipsis">
      ResultDataT
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult" class="md-nav__link">
    <span class="md-ellipsis">
      StreamedRunResult
    </span>
  </a>
  
    <nav class="md-nav" aria-label="StreamedRunResult">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.is_complete" class="md-nav__link">
    <span class="md-ellipsis">
      is_complete
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.all_messages" class="md-nav__link">
    <span class="md-ellipsis">
      all_messages
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.all_messages_json" class="md-nav__link">
    <span class="md-ellipsis">
      all_messages_json
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.new_messages" class="md-nav__link">
    <span class="md-ellipsis">
      new_messages
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.new_messages_json" class="md-nav__link">
    <span class="md-ellipsis">
      new_messages_json
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.stream" class="md-nav__link">
    <span class="md-ellipsis">
      stream
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.stream_text" class="md-nav__link">
    <span class="md-ellipsis">
      stream_text
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.stream_structured" class="md-nav__link">
    <span class="md-ellipsis">
      stream_structured
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.get_data" class="md-nav__link">
    <span class="md-ellipsis">
      get_data
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.usage" class="md-nav__link">
    <span class="md-ellipsis">
      usage
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.validate_structured_result" class="md-nav__link">
    <span class="md-ellipsis">
      validate_structured_result
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
  <a href="#pydantic_ai.result" class="md-nav__link">
    <span class="md-ellipsis">
      result
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.result.ResultDataT" class="md-nav__link">
    <span class="md-ellipsis">
      ResultDataT
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult" class="md-nav__link">
    <span class="md-ellipsis">
      StreamedRunResult
    </span>
  </a>
  
    <nav class="md-nav" aria-label="StreamedRunResult">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.is_complete" class="md-nav__link">
    <span class="md-ellipsis">
      is_complete
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.all_messages" class="md-nav__link">
    <span class="md-ellipsis">
      all_messages
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.all_messages_json" class="md-nav__link">
    <span class="md-ellipsis">
      all_messages_json
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.new_messages" class="md-nav__link">
    <span class="md-ellipsis">
      new_messages
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.new_messages_json" class="md-nav__link">
    <span class="md-ellipsis">
      new_messages_json
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.stream" class="md-nav__link">
    <span class="md-ellipsis">
      stream
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.stream_text" class="md-nav__link">
    <span class="md-ellipsis">
      stream_text
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.stream_structured" class="md-nav__link">
    <span class="md-ellipsis">
      stream_structured
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.get_data" class="md-nav__link">
    <span class="md-ellipsis">
      get_data
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.usage" class="md-nav__link">
    <span class="md-ellipsis">
      usage
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.result.StreamedRunResult.validate_structured_result" class="md-nav__link">
    <span class="md-ellipsis">
      validate_structured_result
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
                
                  


  
  


<h1 id="pydantic_airesult"><code>pydantic_ai.result</code></h1>


<div class="doc doc-object doc-module">



<a id="pydantic_ai.result"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.result.ResultDataT" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ResultDataT</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="n">ResultDataT</span> <span class="o">=</span> <span class="n"><span title="typing_extensions.TypeVar">TypeVar</span></span><span class="p">(</span>
    <span class="s2">"ResultDataT"</span><span class="p">,</span> <span class="n"><span title="typing_extensions.TypeVar(default)">default</span></span><span class="o">=</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><span title="typing_extensions.TypeVar(covariant)">covariant</span></span><span class="o">=</span><span class="kc">True</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Covariant type variable for the result data type of a run.</p>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.result.StreamedRunResult" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">StreamedRunResult</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.tools.AgentDepsT" href="../tools/#pydantic_ai.tools.AgentDepsT">AgentDepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="#pydantic_ai.result.ResultDataT">ResultDataT</a>]</code></p>


        <p>Result of a streamed run that returns structured data via a tool call.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/result.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">173</span>
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
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span>
<span class="normal">390</span>
<span class="normal">391</span>
<span class="normal">392</span>
<span class="normal">393</span>
<span class="normal">394</span>
<span class="normal">395</span>
<span class="normal">396</span>
<span class="normal">397</span>
<span class="normal">398</span>
<span class="normal">399</span>
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
<span class="normal">419</span>
<span class="normal">420</span>
<span class="normal">421</span>
<span class="normal">422</span>
<span class="normal">423</span>
<span class="normal">424</span>
<span class="normal">425</span>
<span class="normal">426</span>
<span class="normal">427</span>
<span class="normal">428</span>
<span class="normal">429</span>
<span class="normal">430</span>
<span class="normal">431</span>
<span class="normal">432</span>
<span class="normal">433</span>
<span class="normal">434</span>
<span class="normal">435</span>
<span class="normal">436</span>
<span class="normal">437</span>
<span class="normal">438</span>
<span class="normal">439</span>
<span class="normal">440</span>
<span class="normal">441</span>
<span class="normal">442</span>
<span class="normal">443</span>
<span class="normal">444</span>
<span class="normal">445</span>
<span class="normal">446</span>
<span class="normal">447</span>
<span class="normal">448</span>
<span class="normal">449</span>
<span class="normal">450</span>
<span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span></pre></div></td><td class="code"><div><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">StreamedRunResult</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Result of a streamed run that returns structured data via a tool call."""</span>

    <span class="n">_all_messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]</span>
    <span class="n">_new_message_index</span><span class="p">:</span> <span class="nb">int</span>

    <span class="n">_usage_limits</span><span class="p">:</span> <span class="n">UsageLimits</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">_stream_response</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">StreamedResponse</span>
    <span class="n">_result_schema</span><span class="p">:</span> <span class="n">_result</span><span class="o">.</span><span class="n">ResultSchema</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">_run_ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">]</span>
    <span class="n">_result_validators</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">_result</span><span class="o">.</span><span class="n">ResultValidator</span><span class="p">[</span><span class="n">AgentDepsT</span><span class="p">,</span> <span class="n">ResultDataT</span><span class="p">]]</span>
    <span class="n">_result_tool_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">_on_complete</span><span class="p">:</span> <span class="n">Callable</span><span class="p">[[],</span> <span class="n">Awaitable</span><span class="p">[</span><span class="kc">None</span><span class="p">]]</span>

    <span class="n">_initial_run_ctx_usage</span><span class="p">:</span> <span class="n">Usage</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">is_complete</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""Whether the stream has all been received.</span>

<span class="sd">    This is set to `True` when one of</span>
<span class="sd">    [`stream`][pydantic_ai.result.StreamedRunResult.stream],</span>
<span class="sd">    [`stream_text`][pydantic_ai.result.StreamedRunResult.stream_text],</span>
<span class="sd">    [`stream_structured`][pydantic_ai.result.StreamedRunResult.stream_structured] or</span>
<span class="sd">    [`get_data`][pydantic_ai.result.StreamedRunResult.get_data] completes.</span>
<span class="sd">    """</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">__post_init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_initial_run_ctx_usage</span> <span class="o">=</span> <span class="n">copy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_run_ctx</span><span class="o">.</span><span class="n">usage</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">all_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return the history of _messages.</span>

<span class="sd">        Args:</span>
<span class="sd">            result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">                This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">                the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">                not be modified.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List of messages.</span>
<span class="sd">        """</span>
        <span class="c1"># this is a method to be consistent with the other methods</span>
        <span class="k">if</span> <span class="n">result_tool_return_content</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s1">'Setting result tool return content is not supported for this result type.'</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_all_messages</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">all_messages_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return all messages from [`all_messages`][pydantic_ai.result.StreamedRunResult.all_messages] as JSON bytes.</span>

<span class="sd">        Args:</span>
<span class="sd">            result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">                This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">                the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">                not be modified.</span>

<span class="sd">        Returns:</span>
<span class="sd">            JSON bytes representing the messages.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessagesTypeAdapter</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">all_messages</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="o">=</span><span class="n">result_tool_return_content</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">new_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return new messages associated with this run.</span>

<span class="sd">        Messages from older runs are excluded.</span>

<span class="sd">        Args:</span>
<span class="sd">            result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">                This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">                the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">                not be modified.</span>

<span class="sd">        Returns:</span>
<span class="sd">            List of new messages.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_messages</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="o">=</span><span class="n">result_tool_return_content</span><span class="p">)[</span><span class="bp">self</span><span class="o">.</span><span class="n">_new_message_index</span> <span class="p">:]</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">new_messages_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return new messages from [`new_messages`][pydantic_ai.result.StreamedRunResult.new_messages] as JSON bytes.</span>

<span class="sd">        Args:</span>
<span class="sd">            result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">                This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">                the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">                not be modified.</span>

<span class="sd">        Returns:</span>
<span class="sd">            JSON bytes representing the new messages.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessagesTypeAdapter</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">new_messages</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="o">=</span><span class="n">result_tool_return_content</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">stream</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">debounce_by</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Stream the response as an async iterable.</span>

<span class="sd">        The pydantic validator for structured data will be called in</span>
<span class="sd">        [partial mode](https://docs.pydantic.dev/dev/concepts/experimental/#partial-validation)</span>
<span class="sd">        on each iteration.</span>

<span class="sd">        Args:</span>
<span class="sd">            debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.</span>
<span class="sd">                Debouncing is particularly important for long structured responses to reduce the overhead of</span>
<span class="sd">                performing validation as each token is received.</span>

<span class="sd">        Returns:</span>
<span class="sd">            An async iterable of the response data.</span>
<span class="sd">        """</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">structured_message</span><span class="p">,</span> <span class="n">is_last</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream_structured</span><span class="p">(</span><span class="n">debounce_by</span><span class="o">=</span><span class="n">debounce_by</span><span class="p">):</span>
            <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_structured_result</span><span class="p">(</span><span class="n">structured_message</span><span class="p">,</span> <span class="n">allow_partial</span><span class="o">=</span><span class="ow">not</span> <span class="n">is_last</span><span class="p">)</span>
            <span class="k">yield</span> <span class="n">result</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">stream_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">delta</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">debounce_by</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Stream the text result as an async iterable.</span>

<span class="sd">        !!! note</span>
<span class="sd">            Result validators will NOT be called on the text result if `delta=True`.</span>

<span class="sd">        Args:</span>
<span class="sd">            delta: if `True`, yield each chunk of text as it is received, if `False` (default), yield the full text</span>
<span class="sd">                up to the current point.</span>
<span class="sd">            debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.</span>
<span class="sd">                Debouncing is particularly important for long structured responses to reduce the overhead of</span>
<span class="sd">                performing validation as each token is received.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span><span class="o">.</span><span class="n">allow_text_result</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">UserError</span><span class="p">(</span><span class="s1">'stream_text() can only be used with text responses'</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">delta</span><span class="p">:</span>
            <span class="k">async</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response_text</span><span class="p">(</span><span class="n">delta</span><span class="o">=</span><span class="n">delta</span><span class="p">,</span> <span class="n">debounce_by</span><span class="o">=</span><span class="n">debounce_by</span><span class="p">):</span>
                <span class="k">yield</span> <span class="n">text</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">async</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response_text</span><span class="p">(</span><span class="n">delta</span><span class="o">=</span><span class="n">delta</span><span class="p">,</span> <span class="n">debounce_by</span><span class="o">=</span><span class="n">debounce_by</span><span class="p">):</span>
                <span class="n">combined_validated_text</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_text_result</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
                <span class="k">yield</span> <span class="n">combined_validated_text</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_marked_completed</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">stream_structured</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">debounce_by</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="mf">0.1</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="nb">tuple</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""Stream the response as an async iterable of Structured LLM Messages.</span>

<span class="sd">        Args:</span>
<span class="sd">            debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.</span>
<span class="sd">                Debouncing is particularly important for long structured responses to reduce the overhead of</span>
<span class="sd">                performing validation as each token is received.</span>

<span class="sd">        Returns:</span>
<span class="sd">            An async iterable of the structured response message and whether that is the last message.</span>
<span class="sd">        """</span>
        <span class="c1"># if the message currently has any parts with content, yield before streaming</span>
        <span class="n">msg</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">msg</span><span class="o">.</span><span class="n">parts</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">part</span><span class="o">.</span><span class="n">has_content</span><span class="p">():</span>
                <span class="k">yield</span> <span class="n">msg</span><span class="p">,</span> <span class="kc">False</span>
                <span class="k">break</span>

        <span class="k">async</span> <span class="k">for</span> <span class="n">msg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response_structured</span><span class="p">(</span><span class="n">debounce_by</span><span class="o">=</span><span class="n">debounce_by</span><span class="p">):</span>
            <span class="k">yield</span> <span class="n">msg</span><span class="p">,</span> <span class="kc">False</span>

        <span class="n">msg</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
        <span class="k">yield</span> <span class="n">msg</span><span class="p">,</span> <span class="kc">True</span>

        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_marked_completed</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">get_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ResultDataT</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Stream the whole response, validate and return it."""</span>
        <span class="n">usage_checking_stream</span> <span class="o">=</span> <span class="n">_get_usage_checking_stream_response</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_usage_limits</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">usage</span>
        <span class="p">)</span>

        <span class="k">async</span> <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">usage_checking_stream</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="n">message</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_marked_completed</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_structured_result</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">usage</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Usage</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the usage of the whole run.</span>

<span class="sd">        !!! note</span>
<span class="sd">            This won't return the full usage until the stream is finished.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_initial_run_ctx_usage</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">usage</span><span class="p">()</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">timestamp</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">datetime</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the timestamp of the response."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">timestamp</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">validate_structured_result</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">allow_partial</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ResultDataT</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Validate a structured result message."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_name</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">match</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span><span class="o">.</span><span class="n">find_named_tool</span><span class="p">(</span><span class="n">message</span><span class="o">.</span><span class="n">parts</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_name</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">match</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
                <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">UnexpectedModelBehavior</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s1">'Invalid response, unable to find tool: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span><span class="o">.</span><span class="n">tool_names</span><span class="p">()</span><span class="si">}</span><span class="s1">'</span>
                <span class="p">)</span>

            <span class="n">call</span><span class="p">,</span> <span class="n">result_tool</span> <span class="o">=</span> <span class="n">match</span>
            <span class="n">result_data</span> <span class="o">=</span> <span class="n">result_tool</span><span class="o">.</span><span class="n">validate</span><span class="p">(</span><span class="n">call</span><span class="p">,</span> <span class="n">allow_partial</span><span class="o">=</span><span class="n">allow_partial</span><span class="p">,</span> <span class="n">wrap_validation_errors</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

            <span class="k">for</span> <span class="n">validator</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_validators</span><span class="p">:</span>
                <span class="n">result_data</span> <span class="o">=</span> <span class="k">await</span> <span class="n">validator</span><span class="o">.</span><span class="n">validate</span><span class="p">(</span><span class="n">result_data</span><span class="p">,</span> <span class="n">call</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_ctx</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">result_data</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="s1">'</span><span class="se">\n\n</span><span class="s1">'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">x</span><span class="o">.</span><span class="n">content</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">message</span><span class="o">.</span><span class="n">parts</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">TextPart</span><span class="p">))</span>
            <span class="k">for</span> <span class="n">validator</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_validators</span><span class="p">:</span>
                <span class="n">text</span> <span class="o">=</span> <span class="k">await</span> <span class="n">validator</span><span class="o">.</span><span class="n">validate</span><span class="p">(</span>
                    <span class="n">text</span><span class="p">,</span>
                    <span class="kc">None</span><span class="p">,</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_run_ctx</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="c1"># Since there is no result tool, we can assume that str is compatible with ResultDataT</span>
            <span class="k">return</span> <span class="n">cast</span><span class="p">(</span><span class="n">ResultDataT</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_validate_text_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">validator</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_validators</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="k">await</span> <span class="n">validator</span><span class="o">.</span><span class="n">validate</span><span class="p">(</span>
                <span class="n">text</span><span class="p">,</span>
                <span class="kc">None</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_run_ctx</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">return</span> <span class="n">text</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_marked_completed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelResponse</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">is_complete</span> <span class="o">=</span> <span class="kc">True</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_all_messages</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_complete</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_stream_response_structured</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">debounce_by</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="mf">0.1</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelResponse</span><span class="p">]:</span>
        <span class="k">async</span> <span class="k">with</span> <span class="n">_utils</span><span class="o">.</span><span class="n">group_by_temporal</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="p">,</span> <span class="n">debounce_by</span><span class="p">)</span> <span class="k">as</span> <span class="n">group_iter</span><span class="p">:</span>
            <span class="k">async</span> <span class="k">for</span> <span class="n">_items</span> <span class="ow">in</span> <span class="n">group_iter</span><span class="p">:</span>
                <span class="k">yield</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_stream_response_text</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">delta</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">debounce_by</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="mf">0.1</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Stream the response as an async iterable of text."""</span>

        <span class="c1"># Define a "merged" version of the iterator that will yield items that have already been retrieved</span>
        <span class="c1"># and items that we receive while streaming. We define a dedicated async iterator for this so we can</span>
        <span class="c1"># pass the combined stream to the group_by_temporal function within `_stream_text_deltas` below.</span>
        <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_stream_text_deltas_ungrouped</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="nb">tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]:</span>
            <span class="c1"># yields tuples of (text_content, part_index)</span>
            <span class="c1"># we don't currently make use of the part_index, but in principle this may be useful</span>
            <span class="c1"># so we retain it here for now to make possible future refactors simpler</span>
            <span class="n">msg</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
            <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">part</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">msg</span><span class="o">.</span><span class="n">parts</span><span class="p">):</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">TextPart</span><span class="p">)</span> <span class="ow">and</span> <span class="n">part</span><span class="o">.</span><span class="n">content</span><span class="p">:</span>
                    <span class="k">yield</span> <span class="n">part</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">i</span>

            <span class="k">async</span> <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="p">:</span>
                <span class="k">if</span> <span class="p">(</span>
                    <span class="nb">isinstance</span><span class="p">(</span><span class="n">event</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">PartStartEvent</span><span class="p">)</span>
                    <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">part</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">TextPart</span><span class="p">)</span>
                    <span class="ow">and</span> <span class="n">event</span><span class="o">.</span><span class="n">part</span><span class="o">.</span><span class="n">content</span>
                <span class="p">):</span>
                    <span class="k">yield</span> <span class="n">event</span><span class="o">.</span><span class="n">part</span><span class="o">.</span><span class="n">content</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">index</span>
                <span class="k">elif</span> <span class="p">(</span>
                    <span class="nb">isinstance</span><span class="p">(</span><span class="n">event</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">PartDeltaEvent</span><span class="p">)</span>
                    <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">delta</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">TextPartDelta</span><span class="p">)</span>
                    <span class="ow">and</span> <span class="n">event</span><span class="o">.</span><span class="n">delta</span><span class="o">.</span><span class="n">content_delta</span>
                <span class="p">):</span>
                    <span class="k">yield</span> <span class="n">event</span><span class="o">.</span><span class="n">delta</span><span class="o">.</span><span class="n">content_delta</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">index</span>

        <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_stream_text_deltas</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
            <span class="k">async</span> <span class="k">with</span> <span class="n">_utils</span><span class="o">.</span><span class="n">group_by_temporal</span><span class="p">(</span><span class="n">_stream_text_deltas_ungrouped</span><span class="p">(),</span> <span class="n">debounce_by</span><span class="p">)</span> <span class="k">as</span> <span class="n">group_iter</span><span class="p">:</span>
                <span class="k">async</span> <span class="k">for</span> <span class="n">items</span> <span class="ow">in</span> <span class="n">group_iter</span><span class="p">:</span>
                    <span class="c1"># Note: we are currently just dropping the part index on the group here</span>
                    <span class="k">yield</span> <span class="s1">''</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">content</span> <span class="k">for</span> <span class="n">content</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">items</span><span class="p">])</span>

        <span class="k">if</span> <span class="n">delta</span><span class="p">:</span>
            <span class="k">async</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">_stream_text_deltas</span><span class="p">():</span>
                <span class="k">yield</span> <span class="n">text</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="c1"># a quick benchmark shows it's faster to build up a string with concat when we're</span>
            <span class="c1"># yielding at each step</span>
            <span class="n">deltas</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">async</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="n">_stream_text_deltas</span><span class="p">():</span>
                <span class="n">deltas</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
                <span class="k">yield</span> <span class="s1">''</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">deltas</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.result.StreamedRunResult.is_complete" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">is_complete</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-class-attribute"><code>class-attribute</code></small>
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="n">is_complete</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="dataclasses.field" href="https://docs.python.org/3/library/dataclasses.html#dataclasses.field">field</a></span><span class="p">(</span><span class="n"><span title="dataclasses.field(default)">default</span></span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n"><span title="dataclasses.field(init)">init</span></span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Whether the stream has all been received.</p>
<p>This is set to <code>True</code> when one of
<a class="autorefs autorefs-internal" href="#pydantic_ai.result.StreamedRunResult.stream"><code>stream</code></a>,
<a class="autorefs autorefs-internal" href="#pydantic_ai.result.StreamedRunResult.stream_text"><code>stream_text</code></a>,
<a class="autorefs autorefs-internal" href="#pydantic_ai.result.StreamedRunResult.stream_structured"><code>stream_structured</code></a> or
<a class="autorefs autorefs-internal" href="#pydantic_ai.result.StreamedRunResult.get_data"><code>get_data</code></a> completes.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.result.StreamedRunResult.all_messages" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">all_messages</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="nf">all_messages</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the history of _messages.</p>


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
                <code>result_tool_return_content</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The return content of the tool call to set in the last message.
This provides a convenient way to modify the content of the result tool call if you want to continue
the conversation and want to set the response to the result tool call. If <code>None</code>, the last message will
not be modified.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


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
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>List of messages.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/result.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">202</span>
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
<span class="normal">217</span></pre></div></td><td class="code"><div><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">all_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Return the history of _messages.</span>

<span class="sd">    Args:</span>
<span class="sd">        result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">            This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">            the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">            not be modified.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List of messages.</span>
<span class="sd">    """</span>
    <span class="c1"># this is a method to be consistent with the other methods</span>
    <span class="k">if</span> <span class="n">result_tool_return_content</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s1">'Setting result tool return content is not supported for this result type.'</span><span class="p">)</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_all_messages</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.result.StreamedRunResult.all_messages_json" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">all_messages_json</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="nf">all_messages_json</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return all messages from <a class="autorefs autorefs-internal" href="#pydantic_ai.result.StreamedRunResult.all_messages"><code>all_messages</code></a> as JSON bytes.</p>


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
                <code>result_tool_return_content</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The return content of the tool call to set in the last message.
This provides a convenient way to modify the content of the result tool call if you want to continue
the conversation and want to set the response to the result tool call. If <code>None</code>, the last message will
not be modified.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


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
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>JSON bytes representing the messages.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/result.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">219</span>
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
<span class="normal">233</span></pre></div></td><td class="code"><div><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">all_messages_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return all messages from [`all_messages`][pydantic_ai.result.StreamedRunResult.all_messages] as JSON bytes.</span>

<span class="sd">    Args:</span>
<span class="sd">        result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">            This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">            the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">            not be modified.</span>

<span class="sd">    Returns:</span>
<span class="sd">        JSON bytes representing the messages.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessagesTypeAdapter</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">all_messages</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="o">=</span><span class="n">result_tool_return_content</span><span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.result.StreamedRunResult.new_messages" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">new_messages</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="nf">new_messages</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return new messages associated with this run.</p>
<p>Messages from older runs are excluded.</p>


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
                <code>result_tool_return_content</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The return content of the tool call to set in the last message.
This provides a convenient way to modify the content of the result tool call if you want to continue
the conversation and want to set the response to the result tool call. If <code>None</code>, the last message will
not be modified.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


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
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>List of new messages.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/result.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">235</span>
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
<span class="normal">249</span></pre></div></td><td class="code"><div><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">new_messages</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Return new messages associated with this run.</span>

<span class="sd">    Messages from older runs are excluded.</span>

<span class="sd">    Args:</span>
<span class="sd">        result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">            This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">            the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">            not be modified.</span>

<span class="sd">    Returns:</span>
<span class="sd">        List of new messages.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">all_messages</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="o">=</span><span class="n">result_tool_return_content</span><span class="p">)[</span><span class="bp">self</span><span class="o">.</span><span class="n">_new_message_index</span> <span class="p">:]</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.result.StreamedRunResult.new_messages_json" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">new_messages_json</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code><span class="nf">new_messages_json</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return new messages from <a class="autorefs autorefs-internal" href="#pydantic_ai.result.StreamedRunResult.new_messages"><code>new_messages</code></a> as JSON bytes.</p>


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
                <code>result_tool_return_content</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The return content of the tool call to set in the last message.
This provides a convenient way to modify the content of the result tool call if you want to continue
the conversation and want to set the response to the result tool call. If <code>None</code>, the last message will
not be modified.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


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
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>JSON bytes representing the new messages.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/result.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">251</span>
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
<span class="normal">265</span></pre></div></td><td class="code"><div><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">new_messages_json</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">result_tool_return_content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return new messages from [`new_messages`][pydantic_ai.result.StreamedRunResult.new_messages] as JSON bytes.</span>

<span class="sd">    Args:</span>
<span class="sd">        result_tool_return_content: The return content of the tool call to set in the last message.</span>
<span class="sd">            This provides a convenient way to modify the content of the result tool call if you want to continue</span>
<span class="sd">            the conversation and want to set the response to the result tool call. If `None`, the last message will</span>
<span class="sd">            not be modified.</span>

<span class="sd">    Returns:</span>
<span class="sd">        JSON bytes representing the new messages.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelMessagesTypeAdapter</span><span class="o">.</span><span class="n">dump_json</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">new_messages</span><span class="p">(</span><span class="n">result_tool_return_content</span><span class="o">=</span><span class="n">result_tool_return_content</span><span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.result.StreamedRunResult.stream" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">stream</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="nf">stream</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span> <span class="n">debounce_by</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="mf">0.1</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="#pydantic_ai.result.ResultDataT">ResultDataT</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Stream the response as an async iterable.</p>
<p>The pydantic validator for structured data will be called in
<a href="https://docs.pydantic.dev/dev/concepts/experimental/#partial-validation">partial mode</a>
on each iteration.</p>


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
                <code>debounce_by</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>by how much (if at all) to debounce/group the response chunks by. <code>None</code> means no debouncing.
Debouncing is particularly important for long structured responses to reduce the overhead of
performing validation as each token is received.</p>
              </div>
            </td>
            <td>
                  <code>0.1</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


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
                  <code><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="#pydantic_ai.result.ResultDataT">ResultDataT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An async iterable of the response data.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/result.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">267</span>
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
<span class="normal">284</span></pre></div></td><td class="code"><div><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code tabindex="0"><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">stream</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">debounce_by</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">ResultDataT</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Stream the response as an async iterable.</span>

<span class="sd">    The pydantic validator for structured data will be called in</span>
<span class="sd">    [partial mode](https://docs.pydantic.dev/dev/concepts/experimental/#partial-validation)</span>
<span class="sd">    on each iteration.</span>

<span class="sd">    Args:</span>
<span class="sd">        debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.</span>
<span class="sd">            Debouncing is particularly important for long structured responses to reduce the overhead of</span>
<span class="sd">            performing validation as each token is received.</span>

<span class="sd">    Returns:</span>
<span class="sd">        An async iterable of the response data.</span>
<span class="sd">    """</span>
    <span class="k">async</span> <span class="k">for</span> <span class="n">structured_message</span><span class="p">,</span> <span class="n">is_last</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">stream_structured</span><span class="p">(</span><span class="n">debounce_by</span><span class="o">=</span><span class="n">debounce_by</span><span class="p">):</span>
        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_structured_result</span><span class="p">(</span><span class="n">structured_message</span><span class="p">,</span> <span class="n">allow_partial</span><span class="o">=</span><span class="ow">not</span> <span class="n">is_last</span><span class="p">)</span>
        <span class="k">yield</span> <span class="n">result</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.result.StreamedRunResult.stream_text" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">stream_text</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="nf">stream_text</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span> <span class="n">delta</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">debounce_by</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="mf">0.1</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Stream the text result as an async iterable.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Result validators will NOT be called on the text result if <code>delta=True</code>.</p>
</div>


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
                <code>delta</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>if <code>True</code>, yield each chunk of text as it is received, if <code>False</code> (default), yield the full text
up to the current point.</p>
              </div>
            </td>
            <td>
                  <code>False</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>debounce_by</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>by how much (if at all) to debounce/group the response chunks by. <code>None</code> means no debouncing.
Debouncing is particularly important for long structured responses to reduce the overhead of
performing validation as each token is received.</p>
              </div>
            </td>
            <td>
                  <code>0.1</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/result.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">286</span>
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
<span class="normal">309</span></pre></div></td><td class="code"><div><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code tabindex="0"><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">stream_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">delta</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">debounce_by</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Stream the text result as an async iterable.</span>

<span class="sd">    !!! note</span>
<span class="sd">        Result validators will NOT be called on the text result if `delta=True`.</span>

<span class="sd">    Args:</span>
<span class="sd">        delta: if `True`, yield each chunk of text as it is received, if `False` (default), yield the full text</span>
<span class="sd">            up to the current point.</span>
<span class="sd">        debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.</span>
<span class="sd">            Debouncing is particularly important for long structured responses to reduce the overhead of</span>
<span class="sd">            performing validation as each token is received.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span><span class="o">.</span><span class="n">allow_text_result</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">UserError</span><span class="p">(</span><span class="s1">'stream_text() can only be used with text responses'</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">delta</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response_text</span><span class="p">(</span><span class="n">delta</span><span class="o">=</span><span class="n">delta</span><span class="p">,</span> <span class="n">debounce_by</span><span class="o">=</span><span class="n">debounce_by</span><span class="p">):</span>
            <span class="k">yield</span> <span class="n">text</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">text</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response_text</span><span class="p">(</span><span class="n">delta</span><span class="o">=</span><span class="n">delta</span><span class="p">,</span> <span class="n">debounce_by</span><span class="o">=</span><span class="n">debounce_by</span><span class="p">):</span>
            <span class="n">combined_validated_text</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_validate_text_result</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
            <span class="k">yield</span> <span class="n">combined_validated_text</span>
    <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_marked_completed</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">get</span><span class="p">())</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.result.StreamedRunResult.stream_structured" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">stream_structured</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="nf">stream_structured</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span> <span class="n">debounce_by</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="mf">0.1</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple">tuple</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponse" href="../messages/#pydantic_ai.messages.ModelResponse">ModelResponse</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span><span class="p">]]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Stream the response as an async iterable of Structured LLM Messages.</p>


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
                <code>debounce_by</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>by how much (if at all) to debounce/group the response chunks by. <code>None</code> means no debouncing.
Debouncing is particularly important for long structured responses to reduce the overhead of
performing validation as each token is received.</p>
              </div>
            </td>
            <td>
                  <code>0.1</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


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
                  <code><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple">tuple</a>[<a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponse" href="../messages/#pydantic_ai.messages.ModelResponse">ModelResponse</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a>]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An async iterable of the structured response message and whether that is the last message.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/result.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">311</span>
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
<span class="normal">337</span></pre></div></td><td class="code"><div><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code tabindex="0"><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">stream_structured</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">debounce_by</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="mf">0.1</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="nb">tuple</span><span class="p">[</span><span class="n">_messages</span><span class="o">.</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""Stream the response as an async iterable of Structured LLM Messages.</span>

<span class="sd">    Args:</span>
<span class="sd">        debounce_by: by how much (if at all) to debounce/group the response chunks by. `None` means no debouncing.</span>
<span class="sd">            Debouncing is particularly important for long structured responses to reduce the overhead of</span>
<span class="sd">            performing validation as each token is received.</span>

<span class="sd">    Returns:</span>
<span class="sd">        An async iterable of the structured response message and whether that is the last message.</span>
<span class="sd">    """</span>
    <span class="c1"># if the message currently has any parts with content, yield before streaming</span>
    <span class="n">msg</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">msg</span><span class="o">.</span><span class="n">parts</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">part</span><span class="o">.</span><span class="n">has_content</span><span class="p">():</span>
            <span class="k">yield</span> <span class="n">msg</span><span class="p">,</span> <span class="kc">False</span>
            <span class="k">break</span>

    <span class="k">async</span> <span class="k">for</span> <span class="n">msg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response_structured</span><span class="p">(</span><span class="n">debounce_by</span><span class="o">=</span><span class="n">debounce_by</span><span class="p">):</span>
        <span class="k">yield</span> <span class="n">msg</span><span class="p">,</span> <span class="kc">False</span>

    <span class="n">msg</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
    <span class="k">yield</span> <span class="n">msg</span><span class="p">,</span> <span class="kc">True</span>

    <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_marked_completed</span><span class="p">(</span><span class="n">msg</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.result.StreamedRunResult.get_data" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">get_data</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="nf">get_data</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="#pydantic_ai.result.ResultDataT">ResultDataT</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Stream the whole response, validate and return it.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/result.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span>
<span class="normal">349</span></pre></div></td><td class="code"><div><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">get_data</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ResultDataT</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Stream the whole response, validate and return it."""</span>
    <span class="n">usage_checking_stream</span> <span class="o">=</span> <span class="n">_get_usage_checking_stream_response</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_usage_limits</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">usage</span>
    <span class="p">)</span>

    <span class="k">async</span> <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="n">usage_checking_stream</span><span class="p">:</span>
        <span class="k">pass</span>
    <span class="n">message</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
    <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_marked_completed</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
    <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">validate_structured_result</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.result.StreamedRunResult.usage" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">usage</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code><span class="nf">usage</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../usage/#pydantic_ai.usage.Usage">Usage</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the usage of the whole run.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>This won't return the full usage until the stream is finished.</p>
</div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/result.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">351</span>
<span class="normal">352</span>
<span class="normal">353</span>
<span class="normal">354</span>
<span class="normal">355</span>
<span class="normal">356</span>
<span class="normal">357</span></pre></div></td><td class="code"><div><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">usage</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Usage</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return the usage of the whole run.</span>

<span class="sd">    !!! note</span>
<span class="sd">        This won't return the full usage until the stream is finished.</span>
<span class="sd">    """</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_initial_run_ctx_usage</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">usage</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.result.StreamedRunResult.timestamp" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">timestamp</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code><span class="nf">timestamp</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="datetime.datetime" href="https://docs.python.org/3/library/datetime.html#datetime.datetime">datetime</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the timestamp of the response.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/result.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">359</span>
<span class="normal">360</span>
<span class="normal">361</span></pre></div></td><td class="code"><div><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">timestamp</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">datetime</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get the timestamp of the response."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_response</span><span class="o">.</span><span class="n">timestamp</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.result.StreamedRunResult.validate_structured_result" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">validate_structured_result</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code><span class="nf">validate_structured_result</span><span class="p">(</span>
    <span class="n">message</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponse" href="../messages/#pydantic_ai.messages.ModelResponse">ModelResponse</a></span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">allow_partial</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">False</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.result.ResultDataT" href="#pydantic_ai.result.ResultDataT">ResultDataT</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Validate a structured result message.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/result.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">363</span>
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
<span class="normal">387</span>
<span class="normal">388</span>
<span class="normal">389</span></pre></div></td><td class="code"><div><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">validate_structured_result</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="n">_messages</span><span class="o">.</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">allow_partial</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ResultDataT</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Validate a structured result message."""</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_name</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">match</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span><span class="o">.</span><span class="n">find_named_tool</span><span class="p">(</span><span class="n">message</span><span class="o">.</span><span class="n">parts</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_tool_name</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">match</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">UnexpectedModelBehavior</span><span class="p">(</span>
                <span class="sa">f</span><span class="s1">'Invalid response, unable to find tool: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_result_schema</span><span class="o">.</span><span class="n">tool_names</span><span class="p">()</span><span class="si">}</span><span class="s1">'</span>
            <span class="p">)</span>

        <span class="n">call</span><span class="p">,</span> <span class="n">result_tool</span> <span class="o">=</span> <span class="n">match</span>
        <span class="n">result_data</span> <span class="o">=</span> <span class="n">result_tool</span><span class="o">.</span><span class="n">validate</span><span class="p">(</span><span class="n">call</span><span class="p">,</span> <span class="n">allow_partial</span><span class="o">=</span><span class="n">allow_partial</span><span class="p">,</span> <span class="n">wrap_validation_errors</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

        <span class="k">for</span> <span class="n">validator</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_validators</span><span class="p">:</span>
            <span class="n">result_data</span> <span class="o">=</span> <span class="k">await</span> <span class="n">validator</span><span class="o">.</span><span class="n">validate</span><span class="p">(</span><span class="n">result_data</span><span class="p">,</span> <span class="n">call</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_ctx</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">result_data</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="s1">'</span><span class="se">\n\n</span><span class="s1">'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">x</span><span class="o">.</span><span class="n">content</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">message</span><span class="o">.</span><span class="n">parts</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">_messages</span><span class="o">.</span><span class="n">TextPart</span><span class="p">))</span>
        <span class="k">for</span> <span class="n">validator</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result_validators</span><span class="p">:</span>
            <span class="n">text</span> <span class="o">=</span> <span class="k">await</span> <span class="n">validator</span><span class="o">.</span><span class="n">validate</span><span class="p">(</span>
                <span class="n">text</span><span class="p">,</span>
                <span class="kc">None</span><span class="p">,</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_run_ctx</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="c1"># Since there is no result tool, we can assume that str is compatible with ResultDataT</span>
        <span class="k">return</span> <span class="n">cast</span><span class="p">(</span><span class="n">ResultDataT</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
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