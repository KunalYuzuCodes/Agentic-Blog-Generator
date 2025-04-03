<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/pydantic_graph/graph/">
      
      
        <link rel="prev" href="../../providers/">
      
      
        <link rel="next" href="../nodes/">
      
      
      <link rel="icon" href="../../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_graph - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_graph - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_graph/graph.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/pydantic_graph/graph/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_graph - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_graph/graph.png">
      
    
    
   <link href="../../../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../../../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#pydantic_graph" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href="../../.." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../../img/logo-white.svg" alt="logo">

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
            
              pydantic_graph
            
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
    <a href="../../.." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../../img/logo-white.svg" alt="logo">

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
      <a href="../../.." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../troubleshooting/" class="md-nav__link">
        
  
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
      <a href="../../../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../../mcp/" class="md-nav__link ">
              
  
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
      <a href="../../../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../cli/" class="md-nav__link">
        
  
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
            <a href="../../../examples/" class="md-nav__link ">
              
  
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
      <a href="../../../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/question-graph/" class="md-nav__link">
        
  
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
      <a href="../../agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.graph" class="md-nav__link">
    <span class="md-ellipsis">
      graph
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph" class="md-nav__link">
    <span class="md-ellipsis">
      Graph
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Graph">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.run" class="md-nav__link">
    <span class="md-ellipsis">
      run
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.run_sync" class="md-nav__link">
    <span class="md-ellipsis">
      run_sync
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.iter" class="md-nav__link">
    <span class="md-ellipsis">
      iter
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.iter_from_persistence" class="md-nav__link">
    <span class="md-ellipsis">
      iter_from_persistence
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.initialize" class="md-nav__link">
    <span class="md-ellipsis">
      initialize
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.next" class="md-nav__link">
    <span class="md-ellipsis">
      next
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.mermaid_code" class="md-nav__link">
    <span class="md-ellipsis">
      mermaid_code
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.mermaid_image" class="md-nav__link">
    <span class="md-ellipsis">
      mermaid_image
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.mermaid_save" class="md-nav__link">
    <span class="md-ellipsis">
      mermaid_save
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.get_nodes" class="md-nav__link">
    <span class="md-ellipsis">
      get_nodes
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRun" class="md-nav__link">
    <span class="md-ellipsis">
      GraphRun
    </span>
  </a>
  
    <nav class="md-nav" aria-label="GraphRun">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRun.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRun.next_node" class="md-nav__link">
    <span class="md-ellipsis">
      next_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRun.result" class="md-nav__link">
    <span class="md-ellipsis">
      result
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRun.next" class="md-nav__link">
    <span class="md-ellipsis">
      next
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRun.__anext__" class="md-nav__link">
    <span class="md-ellipsis">
      __anext__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRunResult" class="md-nav__link">
    <span class="md-ellipsis">
      GraphRunResult
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/generation/" class="md-nav__link">
        
  
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
  <a href="#pydantic_graph.graph" class="md-nav__link">
    <span class="md-ellipsis">
      graph
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph" class="md-nav__link">
    <span class="md-ellipsis">
      Graph
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Graph">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.run" class="md-nav__link">
    <span class="md-ellipsis">
      run
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.run_sync" class="md-nav__link">
    <span class="md-ellipsis">
      run_sync
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.iter" class="md-nav__link">
    <span class="md-ellipsis">
      iter
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.iter_from_persistence" class="md-nav__link">
    <span class="md-ellipsis">
      iter_from_persistence
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.initialize" class="md-nav__link">
    <span class="md-ellipsis">
      initialize
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.next" class="md-nav__link">
    <span class="md-ellipsis">
      next
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.mermaid_code" class="md-nav__link">
    <span class="md-ellipsis">
      mermaid_code
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.mermaid_image" class="md-nav__link">
    <span class="md-ellipsis">
      mermaid_image
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.mermaid_save" class="md-nav__link">
    <span class="md-ellipsis">
      mermaid_save
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.Graph.get_nodes" class="md-nav__link">
    <span class="md-ellipsis">
      get_nodes
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRun" class="md-nav__link">
    <span class="md-ellipsis">
      GraphRun
    </span>
  </a>
  
    <nav class="md-nav" aria-label="GraphRun">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRun.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRun.next_node" class="md-nav__link">
    <span class="md-ellipsis">
      next_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRun.result" class="md-nav__link">
    <span class="md-ellipsis">
      result
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRun.next" class="md-nav__link">
    <span class="md-ellipsis">
      next
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRun.__anext__" class="md-nav__link">
    <span class="md-ellipsis">
      __anext__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.graph.GraphRunResult" class="md-nav__link">
    <span class="md-ellipsis">
      GraphRunResult
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


<h1 id="pydantic_graph"><code>pydantic_graph</code></h1>


<div class="doc doc-object doc-module">



<a id="pydantic_graph.graph"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">























































<div class="doc doc-object doc-class">



<h3 id="pydantic_graph.graph.Graph" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">Graph</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code></p>


        <p>Definition of a graph.</p>
<p>In <code>pydantic-graph</code>, a graph is a collection of nodes that can be run in sequence. The nodes define
their outgoing edges — e.g. which nodes may be run next, and thereby the structure of the graph.</p>
<p>Here's a very simple example of a graph which increments a number by 1, but makes sure the number is never
42 at the end.</p>
<p></p><div class="language-py highlight"><span class="filename">never_42.py</span><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">__future__</span><span class="w"> </span><span class="kn">import</span> <span class="n">annotations</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">dataclasses</span><span class="w"> </span><span class="kn">import</span> <span class="n">dataclass</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_graph</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseNode</span><span class="p">,</span> <span class="n">End</span><span class="p">,</span> <span class="n">Graph</span><span class="p">,</span> <span class="n">GraphRunContext</span>

<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">MyState</span><span class="p">:</span>
    <span class="n">number</span><span class="p">:</span> <span class="nb">int</span>

<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Increment</span><span class="p">(</span><span class="n">BaseNode</span><span class="p">[</span><span class="n">MyState</span><span class="p">]):</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">GraphRunContext</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Check42</span><span class="p">:</span>
        <span class="n">ctx</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">number</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">return</span> <span class="n">Check42</span><span class="p">()</span>

<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Check42</span><span class="p">(</span><span class="n">BaseNode</span><span class="p">[</span><span class="n">MyState</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="nb">int</span><span class="p">]):</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">GraphRunContext</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Increment</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="nb">int</span><span class="p">]:</span>
        <span class="k">if</span> <span class="n">ctx</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">number</span> <span class="o">==</span> <span class="mi">42</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Increment</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">End</span><span class="p">(</span><span class="n">ctx</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">number</span><span class="p">)</span>

<span class="n">never_42_graph</span> <span class="o">=</span> <span class="n">Graph</span><span class="p">(</span><span class="n">nodes</span><span class="o">=</span><span class="p">(</span><span class="n">Increment</span><span class="p">,</span> <span class="n">Check42</span><span class="p">))</span>
</code></pre></div>
<em>(This example is complete, it can be run "as is")</em><p></p>
<p>See <a class="autorefs autorefs-internal" href="#pydantic_graph.graph.Graph.run"><code>run</code></a> For an example of running graph, and
<a class="autorefs autorefs-internal" href="#pydantic_graph.graph.Graph.mermaid_code"><code>mermaid_code</code></a> for an example of generating a mermaid diagram
from the graph.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
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
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span>
<span class="normal">475</span>
<span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span>
<span class="normal">498</span>
<span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span>
<span class="normal">502</span>
<span class="normal">503</span>
<span class="normal">504</span>
<span class="normal">505</span>
<span class="normal">506</span>
<span class="normal">507</span>
<span class="normal">508</span>
<span class="normal">509</span>
<span class="normal">510</span>
<span class="normal">511</span>
<span class="normal">512</span>
<span class="normal">513</span>
<span class="normal">514</span>
<span class="normal">515</span>
<span class="normal">516</span>
<span class="normal">517</span>
<span class="normal">518</span>
<span class="normal">519</span>
<span class="normal">520</span>
<span class="normal">521</span>
<span class="normal">522</span>
<span class="normal">523</span>
<span class="normal">524</span>
<span class="normal">525</span>
<span class="normal">526</span>
<span class="normal">527</span>
<span class="normal">528</span>
<span class="normal">529</span>
<span class="normal">530</span>
<span class="normal">531</span>
<span class="normal">532</span>
<span class="normal">533</span>
<span class="normal">534</span>
<span class="normal">535</span>
<span class="normal">536</span>
<span class="normal">537</span>
<span class="normal">538</span>
<span class="normal">539</span>
<span class="normal">540</span>
<span class="normal">541</span>
<span class="normal">542</span>
<span class="normal">543</span>
<span class="normal">544</span>
<span class="normal">545</span>
<span class="normal">546</span>
<span class="normal">547</span>
<span class="normal">548</span>
<span class="normal">549</span>
<span class="normal">550</span>
<span class="normal">551</span>
<span class="normal">552</span>
<span class="normal">553</span>
<span class="normal">554</span>
<span class="normal">555</span>
<span class="normal">556</span>
<span class="normal">557</span>
<span class="normal">558</span>
<span class="normal">559</span>
<span class="normal">560</span>
<span class="normal">561</span>
<span class="normal">562</span>
<span class="normal">563</span>
<span class="normal">564</span>
<span class="normal">565</span>
<span class="normal">566</span>
<span class="normal">567</span>
<span class="normal">568</span>
<span class="normal">569</span>
<span class="normal">570</span>
<span class="normal">571</span>
<span class="normal">572</span>
<span class="normal">573</span>
<span class="normal">574</span>
<span class="normal">575</span>
<span class="normal">576</span>
<span class="normal">577</span>
<span class="normal">578</span>
<span class="normal">579</span>
<span class="normal">580</span>
<span class="normal">581</span>
<span class="normal">582</span>
<span class="normal">583</span>
<span class="normal">584</span>
<span class="normal">585</span>
<span class="normal">586</span></pre></div></td><td class="code"><div><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code tabindex="0"><span class="nd">@dataclass</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Graph</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Definition of a graph.</span>

<span class="sd">    In `pydantic-graph`, a graph is a collection of nodes that can be run in sequence. The nodes define</span>
<span class="sd">    their outgoing edges — e.g. which nodes may be run next, and thereby the structure of the graph.</span>

<span class="sd">    Here's a very simple example of a graph which increments a number by 1, but makes sure the number is never</span>
<span class="sd">    42 at the end.</span>

<span class="sd">    ```py {title="never_42.py" noqa="I001" py="3.10"}</span>
<span class="sd">    from __future__ import annotations</span>

<span class="sd">    from dataclasses import dataclass</span>

<span class="sd">    from pydantic_graph import BaseNode, End, Graph, GraphRunContext</span>

<span class="sd">    @dataclass</span>
<span class="sd">    class MyState:</span>
<span class="sd">        number: int</span>

<span class="sd">    @dataclass</span>
<span class="sd">    class Increment(BaseNode[MyState]):</span>
<span class="sd">        async def run(self, ctx: GraphRunContext) -&gt; Check42:</span>
<span class="sd">            ctx.state.number += 1</span>
<span class="sd">            return Check42()</span>

<span class="sd">    @dataclass</span>
<span class="sd">    class Check42(BaseNode[MyState, None, int]):</span>
<span class="sd">        async def run(self, ctx: GraphRunContext) -&gt; Increment | End[int]:</span>
<span class="sd">            if ctx.state.number == 42:</span>
<span class="sd">                return Increment()</span>
<span class="sd">            else:</span>
<span class="sd">                return End(ctx.state.number)</span>

<span class="sd">    never_42_graph = Graph(nodes=(Increment, Check42))</span>
<span class="sd">    ```</span>
<span class="sd">    _(This example is complete, it can be run "as is")_</span>

<span class="sd">    See [`run`][pydantic_graph.graph.Graph.run] For an example of running graph, and</span>
<span class="sd">    [`mermaid_code`][pydantic_graph.graph.Graph.mermaid_code] for an example of generating a mermaid diagram</span>
<span class="sd">    from the graph.</span>
<span class="sd">    """</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">node_defs</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NodeDef</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]</span>
    <span class="n">_state_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">StateT</span><span class="p">]</span> <span class="o">|</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_run_end_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">auto_instrument</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]],</span>
        <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">state_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">StateT</span><span class="p">]</span> <span class="o">|</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span><span class="p">,</span>
        <span class="n">run_end_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span><span class="p">,</span>
        <span class="n">auto_instrument</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Create a graph from a sequence of nodes.</span>

<span class="sd">        Args:</span>
<span class="sd">            nodes: The nodes which make up the graph, nodes need to be unique and all be generic in the same</span>
<span class="sd">                state type.</span>
<span class="sd">            name: Optional name for the graph, if not provided the name will be inferred from the calling frame</span>
<span class="sd">                on the first call to a graph method.</span>
<span class="sd">            state_type: The type of the state for the graph, this can generally be inferred from `nodes`.</span>
<span class="sd">            run_end_type: The type of the result of running the graph, this can generally be inferred from `nodes`.</span>
<span class="sd">            auto_instrument: Whether to create a span for the graph run and the execution of each node's run method.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_state_type</span> <span class="o">=</span> <span class="n">state_type</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_run_end_type</span> <span class="o">=</span> <span class="n">run_end_type</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">auto_instrument</span> <span class="o">=</span> <span class="n">auto_instrument</span>

        <span class="n">parent_namespace</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">get_parent_namespace</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">node_defs</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_register_node</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">parent_namespace</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_validate_edges</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">start_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">DepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">span</span><span class="p">:</span> <span class="n">LogfireSpan</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">GraphRunResult</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run the graph from a starting node until it ends.</span>

<span class="sd">        Args:</span>
<span class="sd">            start_node: the first node to run, since the graph definition doesn't define the entry point in the graph,</span>
<span class="sd">                you need to provide the starting node.</span>
<span class="sd">            state: The initial state of the graph.</span>
<span class="sd">            deps: The dependencies of the graph.</span>
<span class="sd">            persistence: State persistence interface, defaults to</span>
<span class="sd">                [`SimpleStatePersistence`][pydantic_graph.SimpleStatePersistence] if `None`.</span>
<span class="sd">            infer_name: Whether to infer the graph name from the calling frame.</span>
<span class="sd">            span: The span to use for the graph run. If not provided, a span will be created depending on the value of</span>
<span class="sd">                the `auto_instrument` field.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A `GraphRunResult` containing information about the run, including its final result.</span>

<span class="sd">        Here's an example of running the graph from [above][pydantic_graph.graph.Graph]:</span>

<span class="sd">        ```py {title="run_never_42.py" noqa="I001" py="3.10"}</span>
<span class="sd">        from never_42 import Increment, MyState, never_42_graph</span>

<span class="sd">        async def main():</span>
<span class="sd">            state = MyState(1)</span>
<span class="sd">            await never_42_graph.run(Increment(), state=state)</span>
<span class="sd">            print(state)</span>
<span class="sd">            #&gt; MyState(number=2)</span>

<span class="sd">            state = MyState(41)</span>
<span class="sd">            await never_42_graph.run(Increment(), state=state)</span>
<span class="sd">            print(state)</span>
<span class="sd">            #&gt; MyState(number=43)</span>
<span class="sd">        ```</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>

        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span>
            <span class="n">start_node</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span> <span class="n">persistence</span><span class="o">=</span><span class="n">persistence</span><span class="p">,</span> <span class="n">span</span><span class="o">=</span><span class="n">span</span><span class="p">,</span> <span class="n">infer_name</span><span class="o">=</span><span class="kc">False</span>
        <span class="p">)</span> <span class="k">as</span> <span class="n">graph_run</span><span class="p">:</span>
            <span class="k">async</span> <span class="k">for</span> <span class="n">_node</span> <span class="ow">in</span> <span class="n">graph_run</span><span class="p">:</span>
                <span class="k">pass</span>

        <span class="n">final_result</span> <span class="o">=</span> <span class="n">graph_run</span><span class="o">.</span><span class="n">result</span>
        <span class="k">assert</span> <span class="n">final_result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'GraphRun should have a final result'</span>
        <span class="k">return</span> <span class="n">final_result</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">run_sync</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">start_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">DepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">GraphRunResult</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Synchronously run the graph.</span>

<span class="sd">        This is a convenience method that wraps [`self.run`][pydantic_graph.Graph.run] with `loop.run_until_complete(...)`.</span>
<span class="sd">        You therefore can't use this method inside async code or if there's an active event loop.</span>

<span class="sd">        Args:</span>
<span class="sd">            start_node: the first node to run, since the graph definition doesn't define the entry point in the graph,</span>
<span class="sd">                you need to provide the starting node.</span>
<span class="sd">            state: The initial state of the graph.</span>
<span class="sd">            deps: The dependencies of the graph.</span>
<span class="sd">            persistence: State persistence interface, defaults to</span>
<span class="sd">                [`SimpleStatePersistence`][pydantic_graph.SimpleStatePersistence] if `None`.</span>
<span class="sd">            infer_name: Whether to infer the graph name from the calling frame.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The result type from ending the run and the history of the run.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>

        <span class="k">return</span> <span class="n">_utils</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">start_node</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span> <span class="n">persistence</span><span class="o">=</span><span class="n">persistence</span><span class="p">,</span> <span class="n">infer_name</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
        <span class="p">)</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">iter</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">start_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">DepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">span</span><span class="p">:</span> <span class="n">AbstractContextManager</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">GraphRun</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""A contextmanager which can be used to iterate over the graph's nodes as they are executed.</span>

<span class="sd">        This method returns a `GraphRun` object which can be used to async-iterate over the nodes of this `Graph` as</span>
<span class="sd">        they are executed. This is the API to use if you want to record or interact with the nodes as the graph</span>
<span class="sd">        execution unfolds.</span>

<span class="sd">        The `GraphRun` can also be used to manually drive the graph execution by calling</span>
<span class="sd">        [`GraphRun.next`][pydantic_graph.graph.GraphRun.next].</span>

<span class="sd">        The `GraphRun` provides access to the full run history, state, deps, and the final result of the run once</span>
<span class="sd">        it has completed.</span>

<span class="sd">        For more details, see the API documentation of [`GraphRun`][pydantic_graph.graph.GraphRun].</span>

<span class="sd">        Args:</span>
<span class="sd">            start_node: the first node to run. Since the graph definition doesn't define the entry point in the graph,</span>
<span class="sd">                you need to provide the starting node.</span>
<span class="sd">            state: The initial state of the graph.</span>
<span class="sd">            deps: The dependencies of the graph.</span>
<span class="sd">            persistence: State persistence interface, defaults to</span>
<span class="sd">                [`SimpleStatePersistence`][pydantic_graph.SimpleStatePersistence] if `None`.</span>
<span class="sd">            span: The span to use for the graph run. If not provided, a new span will be created.</span>
<span class="sd">            infer_name: Whether to infer the graph name from the calling frame.</span>

<span class="sd">        Returns: A GraphRun that can be async iterated over to drive the graph to completion.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># f_back because `asynccontextmanager` adds one frame</span>
            <span class="k">if</span> <span class="n">frame</span> <span class="o">:=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">():</span>  <span class="c1"># pragma: no branch</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">frame</span><span class="o">.</span><span class="n">f_back</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">persistence</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">persistence</span> <span class="o">=</span> <span class="n">SimpleStatePersistence</span><span class="p">()</span>
        <span class="n">persistence</span><span class="o">.</span><span class="n">set_graph_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">auto_instrument</span> <span class="ow">and</span> <span class="n">span</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">span</span> <span class="o">=</span> <span class="n">logfire_api</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'run graph </span><span class="si">{graph.name}</span><span class="s1">'</span><span class="p">,</span> <span class="n">graph</span><span class="o">=</span><span class="bp">self</span><span class="p">)</span>

        <span class="k">with</span> <span class="n">ExitStack</span><span class="p">()</span> <span class="k">as</span> <span class="n">stack</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">span</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">stack</span><span class="o">.</span><span class="n">enter_context</span><span class="p">(</span><span class="n">span</span><span class="p">)</span>
            <span class="k">yield</span> <span class="n">GraphRun</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">](</span>
                <span class="n">graph</span><span class="o">=</span><span class="bp">self</span><span class="p">,</span> <span class="n">start_node</span><span class="o">=</span><span class="n">start_node</span><span class="p">,</span> <span class="n">persistence</span><span class="o">=</span><span class="n">persistence</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">deps</span>
            <span class="p">)</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">iter_from_persistence</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">DepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">span</span><span class="p">:</span> <span class="n">AbstractContextManager</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">GraphRun</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]:</span>
<span class="w">        </span><span class="sd">"""A contextmanager to iterate over the graph's nodes as they are executed, created from a persistence object.</span>

<span class="sd">        This method has similar functionality to [`iter`][pydantic_graph.graph.Graph.iter],</span>
<span class="sd">        but instead of passing the node to run, it will restore the node and state from state persistence.</span>

<span class="sd">        Args:</span>
<span class="sd">            persistence: The state persistence interface to use.</span>
<span class="sd">            deps: The dependencies of the graph.</span>
<span class="sd">            span: The span to use for the graph run. If not provided, a new span will be created.</span>
<span class="sd">            infer_name: Whether to infer the graph name from the calling frame.</span>

<span class="sd">        Returns: A GraphRun that can be async iterated over to drive the graph to completion.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># f_back because `asynccontextmanager` adds one frame</span>
            <span class="k">if</span> <span class="n">frame</span> <span class="o">:=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">():</span>  <span class="c1"># pragma: no branch</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">frame</span><span class="o">.</span><span class="n">f_back</span><span class="p">)</span>

        <span class="n">persistence</span><span class="o">.</span><span class="n">set_graph_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>

        <span class="n">snapshot</span> <span class="o">=</span> <span class="k">await</span> <span class="n">persistence</span><span class="o">.</span><span class="n">load_next</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">snapshot</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">GraphRuntimeError</span><span class="p">(</span><span class="s1">'Unable to restore snapshot from state persistence.'</span><span class="p">)</span>

        <span class="n">snapshot</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">set_snapshot_id</span><span class="p">(</span><span class="n">snapshot</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>

        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">auto_instrument</span> <span class="ow">and</span> <span class="n">span</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">span</span> <span class="o">=</span> <span class="n">logfire_api</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'run graph </span><span class="si">{graph.name}</span><span class="s1">'</span><span class="p">,</span> <span class="n">graph</span><span class="o">=</span><span class="bp">self</span><span class="p">)</span>

        <span class="k">with</span> <span class="n">ExitStack</span><span class="p">()</span> <span class="k">as</span> <span class="n">stack</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">span</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="n">stack</span><span class="o">.</span><span class="n">enter_context</span><span class="p">(</span><span class="n">span</span><span class="p">)</span>
            <span class="k">yield</span> <span class="n">GraphRun</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">](</span>
                <span class="n">graph</span><span class="o">=</span><span class="bp">self</span><span class="p">,</span>
                <span class="n">start_node</span><span class="o">=</span><span class="n">snapshot</span><span class="o">.</span><span class="n">node</span><span class="p">,</span>
                <span class="n">persistence</span><span class="o">=</span><span class="n">persistence</span><span class="p">,</span>
                <span class="n">state</span><span class="o">=</span><span class="n">snapshot</span><span class="o">.</span><span class="n">state</span><span class="p">,</span>
                <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span>
                <span class="n">snapshot_id</span><span class="o">=</span><span class="n">snapshot</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">initialize</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
        <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize a new graph run in persistence without running it.</span>

<span class="sd">        This is useful if you want to set up a graph run to be run later, e.g. via</span>
<span class="sd">        [`iter_from_persistence`][pydantic_graph.graph.Graph.iter_from_persistence].</span>

<span class="sd">        Args:</span>
<span class="sd">            node: The node to run first.</span>
<span class="sd">            persistence: State persistence interface.</span>
<span class="sd">            state: The start state of the graph.</span>
<span class="sd">            infer_name: Whether to infer the graph name from the calling frame.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>

        <span class="n">persistence</span><span class="o">.</span><span class="n">set_graph_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
        <span class="k">await</span> <span class="n">persistence</span><span class="o">.</span><span class="n">snapshot_node</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span>

    <span class="nd">@deprecated</span><span class="p">(</span><span class="s1">'`next` is deprecated, use `async with graph.iter(...) as run:  run.next()` instead'</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">next</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
        <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">DepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Run a node in the graph and return the next node to run.</span>

<span class="sd">        Args:</span>
<span class="sd">            node: The node to run.</span>
<span class="sd">            persistence: State persistence interface, defaults to</span>
<span class="sd">                [`SimpleStatePersistence`][pydantic_graph.SimpleStatePersistence] if `None`.</span>
<span class="sd">            state: The current state of the graph.</span>
<span class="sd">            deps: The dependencies of the graph.</span>
<span class="sd">            infer_name: Whether to infer the graph name from the calling frame.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The next node to run or [`End`][pydantic_graph.nodes.End] if the graph has finished.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>

        <span class="n">persistence</span><span class="o">.</span><span class="n">set_graph_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
        <span class="n">run</span> <span class="o">=</span> <span class="n">GraphRun</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">](</span>
            <span class="n">graph</span><span class="o">=</span><span class="bp">self</span><span class="p">,</span>
            <span class="n">start_node</span><span class="o">=</span><span class="n">node</span><span class="p">,</span>
            <span class="n">persistence</span><span class="o">=</span><span class="n">persistence</span><span class="p">,</span>
            <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span>
            <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="k">return</span> <span class="k">await</span> <span class="n">run</span><span class="o">.</span><span class="n">next</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">mermaid_code</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">start_node</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">mermaid</span><span class="o">.</span><span class="n">NodeIdent</span><span class="p">]</span> <span class="o">|</span> <span class="n">mermaid</span><span class="o">.</span><span class="n">NodeIdent</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">title</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">|</span> <span class="n">typing_extensions</span><span class="o">.</span><span class="n">Literal</span><span class="p">[</span><span class="kc">False</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">edge_labels</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">notes</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">highlighted_nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">mermaid</span><span class="o">.</span><span class="n">NodeIdent</span><span class="p">]</span> <span class="o">|</span> <span class="n">mermaid</span><span class="o">.</span><span class="n">NodeIdent</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">highlight_css</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">mermaid</span><span class="o">.</span><span class="n">DEFAULT_HIGHLIGHT_CSS</span><span class="p">,</span>
        <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
        <span class="n">direction</span><span class="p">:</span> <span class="n">mermaid</span><span class="o">.</span><span class="n">StateDiagramDirection</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generate a diagram representing the graph as [mermaid](https://mermaid.js.org/) diagram.</span>

<span class="sd">        This method calls [`pydantic_graph.mermaid.generate_code`][pydantic_graph.mermaid.generate_code].</span>

<span class="sd">        Args:</span>
<span class="sd">            start_node: The node or nodes which can start the graph.</span>
<span class="sd">            title: The title of the diagram, use `False` to not include a title.</span>
<span class="sd">            edge_labels: Whether to include edge labels.</span>
<span class="sd">            notes: Whether to include notes on each node.</span>
<span class="sd">            highlighted_nodes: Optional node or nodes to highlight.</span>
<span class="sd">            highlight_css: The CSS to use for highlighting nodes.</span>
<span class="sd">            infer_name: Whether to infer the graph name from the calling frame.</span>
<span class="sd">            direction: The direction of flow.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The mermaid code for the graph, which can then be rendered as a diagram.</span>

<span class="sd">        Here's an example of generating a diagram for the graph from [above][pydantic_graph.graph.Graph]:</span>

<span class="sd">        ```py {title="mermaid_never_42.py" py="3.10"}</span>
<span class="sd">        from never_42 import Increment, never_42_graph</span>

<span class="sd">        print(never_42_graph.mermaid_code(start_node=Increment))</span>
<span class="sd">        '''</span>
<span class="sd">        ---</span>
<span class="sd">        title: never_42_graph</span>
<span class="sd">        ---</span>
<span class="sd">        stateDiagram-v2</span>
<span class="sd">          [*] --&gt; Increment</span>
<span class="sd">          Increment --&gt; Check42</span>
<span class="sd">          Check42 --&gt; Increment</span>
<span class="sd">          Check42 --&gt; [*]</span>
<span class="sd">        '''</span>
<span class="sd">        ```</span>

<span class="sd">        The rendered diagram will look like this:</span>

<span class="sd">        ```mermaid</span>
<span class="sd">        ---</span>
<span class="sd">        title: never_42_graph</span>
<span class="sd">        ---</span>
<span class="sd">        stateDiagram-v2</span>
<span class="sd">          [*] --&gt; Increment</span>
<span class="sd">          Increment --&gt; Check42</span>
<span class="sd">          Check42 --&gt; Increment</span>
<span class="sd">          Check42 --&gt; [*]</span>
<span class="sd">        ```</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
        <span class="k">if</span> <span class="n">title</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">:</span>
            <span class="n">title</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span>
        <span class="k">return</span> <span class="n">mermaid</span><span class="o">.</span><span class="n">generate_code</span><span class="p">(</span>
            <span class="bp">self</span><span class="p">,</span>
            <span class="n">start_node</span><span class="o">=</span><span class="n">start_node</span><span class="p">,</span>
            <span class="n">highlighted_nodes</span><span class="o">=</span><span class="n">highlighted_nodes</span><span class="p">,</span>
            <span class="n">highlight_css</span><span class="o">=</span><span class="n">highlight_css</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="n">title</span> <span class="ow">or</span> <span class="kc">None</span><span class="p">,</span>
            <span class="n">edge_labels</span><span class="o">=</span><span class="n">edge_labels</span><span class="p">,</span>
            <span class="n">notes</span><span class="o">=</span><span class="n">notes</span><span class="p">,</span>
            <span class="n">direction</span><span class="o">=</span><span class="n">direction</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">mermaid_image</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">typing_extensions</span><span class="o">.</span><span class="n">Unpack</span><span class="p">[</span><span class="n">mermaid</span><span class="o">.</span><span class="n">MermaidConfig</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generate a diagram representing the graph as an image.</span>

<span class="sd">        The format and diagram can be customized using `kwargs`,</span>
<span class="sd">        see [`pydantic_graph.mermaid.MermaidConfig`][pydantic_graph.mermaid.MermaidConfig].</span>

<span class="sd">        !!! note "Uses external service"</span>
<span class="sd">            This method makes a request to [mermaid.ink](https://mermaid.ink) to render the image, `mermaid.ink`</span>
<span class="sd">            is a free service not affiliated with Pydantic.</span>

<span class="sd">        Args:</span>
<span class="sd">            infer_name: Whether to infer the graph name from the calling frame.</span>
<span class="sd">            **kwargs: Additional arguments to pass to `mermaid.request_image`.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The image bytes.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
        <span class="k">if</span> <span class="s1">'title'</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">kwargs</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">:</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s1">'title'</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span>
        <span class="k">return</span> <span class="n">mermaid</span><span class="o">.</span><span class="n">request_image</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">mermaid_save</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span><span class="p">,</span> <span class="o">/</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">typing_extensions</span><span class="o">.</span><span class="n">Unpack</span><span class="p">[</span><span class="n">mermaid</span><span class="o">.</span><span class="n">MermaidConfig</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Generate a diagram representing the graph and save it as an image.</span>

<span class="sd">        The format and diagram can be customized using `kwargs`,</span>
<span class="sd">        see [`pydantic_graph.mermaid.MermaidConfig`][pydantic_graph.mermaid.MermaidConfig].</span>

<span class="sd">        !!! note "Uses external service"</span>
<span class="sd">            This method makes a request to [mermaid.ink](https://mermaid.ink) to render the image, `mermaid.ink`</span>
<span class="sd">            is a free service not affiliated with Pydantic.</span>

<span class="sd">        Args:</span>
<span class="sd">            path: The path to save the image to.</span>
<span class="sd">            infer_name: Whether to infer the graph name from the calling frame.</span>
<span class="sd">            **kwargs: Additional arguments to pass to `mermaid.save_image`.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
        <span class="k">if</span> <span class="s1">'title'</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">kwargs</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">:</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s1">'title'</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span>
        <span class="n">mermaid</span><span class="o">.</span><span class="n">save_image</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">get_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]]:</span>
<span class="w">        </span><span class="sd">"""Get the nodes in the graph."""</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">node_def</span><span class="o">.</span><span class="n">node</span> <span class="k">for</span> <span class="n">node_def</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_defs</span><span class="o">.</span><span class="n">values</span><span class="p">()]</span>

    <span class="nd">@cached_property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">inferred_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">StateT</span><span class="p">],</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]]:</span>
        <span class="c1"># Get the types of the state and run end from the graph.</span>
        <span class="k">if</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_state_type</span><span class="p">)</span> <span class="ow">and</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_run_end_type</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_state_type</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_end_type</span>

        <span class="n">state_type</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_state_type</span>
        <span class="n">run_end_type</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_end_type</span>

        <span class="k">for</span> <span class="n">node_def</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_defs</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
            <span class="k">for</span> <span class="n">base</span> <span class="ow">in</span> <span class="n">typing_extensions</span><span class="o">.</span><span class="n">get_original_bases</span><span class="p">(</span><span class="n">node_def</span><span class="o">.</span><span class="n">node</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">typing_extensions</span><span class="o">.</span><span class="n">get_origin</span><span class="p">(</span><span class="n">base</span><span class="p">)</span> <span class="ow">is</span> <span class="n">BaseNode</span><span class="p">:</span>
                    <span class="n">args</span> <span class="o">=</span> <span class="n">typing_extensions</span><span class="o">.</span><span class="n">get_args</span><span class="p">(</span><span class="n">base</span><span class="p">)</span>
                    <span class="k">if</span> <span class="ow">not</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">state_type</span><span class="p">)</span> <span class="ow">and</span> <span class="n">args</span><span class="p">:</span>
                        <span class="n">state_type</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

                    <span class="k">if</span> <span class="ow">not</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">run_end_type</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">==</span> <span class="mi">3</span><span class="p">:</span>
                        <span class="n">t</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
                        <span class="k">if</span> <span class="ow">not</span> <span class="n">typing_objects</span><span class="o">.</span><span class="n">is_never</span><span class="p">(</span><span class="n">t</span><span class="p">):</span>
                            <span class="n">run_end_type</span> <span class="o">=</span> <span class="n">t</span>
                    <span class="k">if</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">state_type</span><span class="p">)</span> <span class="ow">and</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">run_end_type</span><span class="p">):</span>
                        <span class="k">return</span> <span class="n">state_type</span><span class="p">,</span> <span class="n">run_end_type</span>  <span class="c1"># pyright: ignore[reportReturnType]</span>
                    <span class="c1"># break the inner (bases) loop</span>
                    <span class="k">break</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">state_type</span><span class="p">):</span>
            <span class="c1"># state defaults to None, so use that if we can't infer it</span>
            <span class="n">state_type</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">_utils</span><span class="o">.</span><span class="n">is_set</span><span class="p">(</span><span class="n">run_end_type</span><span class="p">):</span>
            <span class="c1"># this happens if a graph has no return nodes, use None so any downstream errors are clear</span>
            <span class="n">run_end_type</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">return</span> <span class="n">state_type</span><span class="p">,</span> <span class="n">run_end_type</span>  <span class="c1"># pyright: ignore[reportReturnType]</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_register_node</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">node</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]],</span>
        <span class="n">parent_namespace</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">node_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_node_id</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">existing_node</span> <span class="o">:=</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_defs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">node_id</span><span class="p">):</span>
            <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">GraphSetupError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s1">'Node ID `</span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s1">` is not unique — found on </span><span class="si">{</span><span class="n">existing_node</span><span class="o">.</span><span class="n">node</span><span class="si">}</span><span class="s1"> and </span><span class="si">{</span><span class="n">node</span><span class="si">}</span><span class="s1">'</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">node_defs</span><span class="p">[</span><span class="n">node_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_node_def</span><span class="p">(</span><span class="n">parent_namespace</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_validate_edges</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">known_node_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_defs</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span>
        <span class="n">bad_edges</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="p">{}</span>

        <span class="k">for</span> <span class="n">node_id</span><span class="p">,</span> <span class="n">node_def</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_defs</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="k">for</span> <span class="n">edge</span> <span class="ow">in</span> <span class="n">node_def</span><span class="o">.</span><span class="n">next_node_edges</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span>
                <span class="k">if</span> <span class="n">edge</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">known_node_ids</span><span class="p">:</span>
                    <span class="n">bad_edges</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">edge</span><span class="p">,</span> <span class="p">[])</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'`</span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s1">`'</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">bad_edges</span><span class="p">:</span>
            <span class="n">bad_edges_list</span> <span class="o">=</span> <span class="p">[</span><span class="sa">f</span><span class="s1">'`</span><span class="si">{</span><span class="n">k</span><span class="si">}</span><span class="s1">` is referenced by </span><span class="si">{</span><span class="n">_utils</span><span class="o">.</span><span class="n">comma_and</span><span class="p">(</span><span class="n">v</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">bad_edges</span><span class="o">.</span><span class="n">items</span><span class="p">()]</span>
            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">bad_edges_list</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
                <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">GraphSetupError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">bad_edges_list</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="si">}</span><span class="s1"> but not included in the graph.'</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">b</span> <span class="o">=</span> <span class="s1">'</span><span class="se">\n</span><span class="s1">'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="sa">f</span><span class="s1">' </span><span class="si">{</span><span class="n">be</span><span class="si">}</span><span class="s1">'</span> <span class="k">for</span> <span class="n">be</span> <span class="ow">in</span> <span class="n">bad_edges_list</span><span class="p">)</span>
                <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">GraphSetupError</span><span class="p">(</span>
                    <span class="sa">f</span><span class="s1">'Nodes are referenced in the graph but not included in the graph:</span><span class="se">\n</span><span class="si">{</span><span class="n">b</span><span class="si">}</span><span class="s1">'</span>
                <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_infer_name</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">function_frame</span><span class="p">:</span> <span class="n">types</span><span class="o">.</span><span class="n">FrameType</span> <span class="o">|</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Infer the agent name from the call frame.</span>

<span class="sd">        Usage should be `self._infer_name(inspect.currentframe())`.</span>

<span class="sd">        Copied from `Agent`.</span>
<span class="sd">        """</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Name already set'</span>
        <span class="k">if</span> <span class="n">function_frame</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="p">(</span><span class="n">parent_frame</span> <span class="o">:=</span> <span class="n">function_frame</span><span class="o">.</span><span class="n">f_back</span><span class="p">):</span>  <span class="c1"># pragma: no branch</span>
            <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">parent_frame</span><span class="o">.</span><span class="n">f_locals</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="k">if</span> <span class="n">item</span> <span class="ow">is</span> <span class="bp">self</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
                    <span class="k">return</span>
            <span class="k">if</span> <span class="n">parent_frame</span><span class="o">.</span><span class="n">f_locals</span> <span class="o">!=</span> <span class="n">parent_frame</span><span class="o">.</span><span class="n">f_globals</span><span class="p">:</span>
                <span class="c1"># if we couldn't find the agent in locals and globals are a different dict, try globals</span>
                <span class="k">for</span> <span class="n">name</span><span class="p">,</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">parent_frame</span><span class="o">.</span><span class="n">f_globals</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                    <span class="k">if</span> <span class="n">item</span> <span class="ow">is</span> <span class="bp">self</span><span class="p">:</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
                        <span class="k">return</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.Graph.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">nodes</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]]],</span>
    <span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">state_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><span title="pydantic_graph._utils.Unset">Unset</span></span> <span class="o">=</span> <span class="n"><span title="pydantic_graph._utils.UNSET">UNSET</span></span><span class="p">,</span>
    <span class="n">run_end_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><span title="pydantic_graph._utils.Unset">Unset</span></span> <span class="o">=</span> <span class="n"><span title="pydantic_graph._utils.UNSET">UNSET</span></span><span class="p">,</span>
    <span class="n">auto_instrument</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a graph from a sequence of nodes.</p>


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
                <code>nodes</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]]]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The nodes which make up the graph, nodes need to be unique and all be generic in the same
state type.</p>
              </div>
            </td>
            <td>
                <em>required</em>
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
                <p>Optional name for the graph, if not provided the name will be inferred from the calling frame
on the first call to a graph method.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>state_type</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>] | <span title="pydantic_graph._utils.Unset">Unset</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The type of the state for the graph, this can generally be inferred from <code>nodes</code>.</p>
              </div>
            </td>
            <td>
                  <code><span title="pydantic_graph._utils.UNSET">UNSET</span></code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>run_end_type</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>] | <span title="pydantic_graph._utils.Unset">Unset</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The type of the result of running the graph, this can generally be inferred from <code>nodes</code>.</p>
              </div>
            </td>
            <td>
                  <code><span title="pydantic_graph._utils.UNSET">UNSET</span></code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>auto_instrument</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to create a span for the graph run and the execution of each node's run method.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span></pre></div></td><td class="code"><div><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]],</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">state_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">StateT</span><span class="p">]</span> <span class="o">|</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span><span class="p">,</span>
    <span class="n">run_end_type</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="n">_utils</span><span class="o">.</span><span class="n">Unset</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">UNSET</span><span class="p">,</span>
    <span class="n">auto_instrument</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Create a graph from a sequence of nodes.</span>

<span class="sd">    Args:</span>
<span class="sd">        nodes: The nodes which make up the graph, nodes need to be unique and all be generic in the same</span>
<span class="sd">            state type.</span>
<span class="sd">        name: Optional name for the graph, if not provided the name will be inferred from the calling frame</span>
<span class="sd">            on the first call to a graph method.</span>
<span class="sd">        state_type: The type of the state for the graph, this can generally be inferred from `nodes`.</span>
<span class="sd">        run_end_type: The type of the result of running the graph, this can generally be inferred from `nodes`.</span>
<span class="sd">        auto_instrument: Whether to create a span for the graph run and the execution of each node's run method.</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_state_type</span> <span class="o">=</span> <span class="n">state_type</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_run_end_type</span> <span class="o">=</span> <span class="n">run_end_type</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">auto_instrument</span> <span class="o">=</span> <span class="n">auto_instrument</span>

    <span class="n">parent_namespace</span> <span class="o">=</span> <span class="n">_utils</span><span class="o">.</span><span class="n">get_parent_namespace</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">node_defs</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">nodes</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_register_node</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">parent_namespace</span><span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_validate_edges</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.Graph.run" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">run</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="nf">run</span><span class="p">(</span>
    <span class="n">start_node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">state</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">span</span><span class="p">:</span> <span class="n"><span title="logfire_api.LogfireSpan">LogfireSpan</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.graph.GraphRunResult" href="#pydantic_graph.graph.GraphRunResult">GraphRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Run the graph from a starting node until it ends.</p>


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
                <code>start_node</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>the first node to run, since the graph definition doesn't define the entry point in the graph,
you need to provide the starting node.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>state</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The initial state of the graph.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>deps</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The dependencies of the graph.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>persistence</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>State persistence interface, defaults to
<a class="autorefs autorefs-internal" href="../persistence/#pydantic_graph.persistence.in_mem.SimpleStatePersistence"><code>SimpleStatePersistence</code></a> if <code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to infer the graph name from the calling frame.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>span</code>
            </td>
            <td>
                  <code><span title="logfire_api.LogfireSpan">LogfireSpan</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The span to use for the graph run. If not provided, a span will be created depending on the value of
the <code>auto_instrument</code> field.</p>
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
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.graph.GraphRunResult" href="#pydantic_graph.graph.GraphRunResult">GraphRunResult</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A <code>GraphRunResult</code> containing information about the run, including its final result.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>
        <p>Here's an example of running the graph from <a class="autorefs autorefs-internal" href="#pydantic_graph.graph.Graph">above</a>:</p>
<div class="language-py highlight"><span class="filename">run_never_42.py</span><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">never_42</span><span class="w"> </span><span class="kn">import</span> <span class="n">Increment</span><span class="p">,</span> <span class="n">MyState</span><span class="p">,</span> <span class="n">never_42_graph</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">state</span> <span class="o">=</span> <span class="n">MyState</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
    <span class="k">await</span> <span class="n">never_42_graph</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">Increment</span><span class="p">(),</span> <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>
    <span class="c1">#&gt; MyState(number=2)</span>

    <span class="n">state</span> <span class="o">=</span> <span class="n">MyState</span><span class="p">(</span><span class="mi">41</span><span class="p">)</span>
    <span class="k">await</span> <span class="n">never_42_graph</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">Increment</span><span class="p">(),</span> <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>
    <span class="c1">#&gt; MyState(number=43)</span>
</code></pre></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span></pre></div></td><td class="code"><div><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code tabindex="0"><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">start_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n">DepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">span</span><span class="p">:</span> <span class="n">LogfireSpan</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">GraphRunResult</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Run the graph from a starting node until it ends.</span>

<span class="sd">    Args:</span>
<span class="sd">        start_node: the first node to run, since the graph definition doesn't define the entry point in the graph,</span>
<span class="sd">            you need to provide the starting node.</span>
<span class="sd">        state: The initial state of the graph.</span>
<span class="sd">        deps: The dependencies of the graph.</span>
<span class="sd">        persistence: State persistence interface, defaults to</span>
<span class="sd">            [`SimpleStatePersistence`][pydantic_graph.SimpleStatePersistence] if `None`.</span>
<span class="sd">        infer_name: Whether to infer the graph name from the calling frame.</span>
<span class="sd">        span: The span to use for the graph run. If not provided, a span will be created depending on the value of</span>
<span class="sd">            the `auto_instrument` field.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A `GraphRunResult` containing information about the run, including its final result.</span>

<span class="sd">    Here's an example of running the graph from [above][pydantic_graph.graph.Graph]:</span>

<span class="sd">    ```py {title="run_never_42.py" noqa="I001" py="3.10"}</span>
<span class="sd">    from never_42 import Increment, MyState, never_42_graph</span>

<span class="sd">    async def main():</span>
<span class="sd">        state = MyState(1)</span>
<span class="sd">        await never_42_graph.run(Increment(), state=state)</span>
<span class="sd">        print(state)</span>
<span class="sd">        #&gt; MyState(number=2)</span>

<span class="sd">        state = MyState(41)</span>
<span class="sd">        await never_42_graph.run(Increment(), state=state)</span>
<span class="sd">        print(state)</span>
<span class="sd">        #&gt; MyState(number=43)</span>
<span class="sd">    ```</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>

    <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span>
        <span class="n">start_node</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span> <span class="n">persistence</span><span class="o">=</span><span class="n">persistence</span><span class="p">,</span> <span class="n">span</span><span class="o">=</span><span class="n">span</span><span class="p">,</span> <span class="n">infer_name</span><span class="o">=</span><span class="kc">False</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">graph_run</span><span class="p">:</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">_node</span> <span class="ow">in</span> <span class="n">graph_run</span><span class="p">:</span>
            <span class="k">pass</span>

    <span class="n">final_result</span> <span class="o">=</span> <span class="n">graph_run</span><span class="o">.</span><span class="n">result</span>
    <span class="k">assert</span> <span class="n">final_result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'GraphRun should have a final result'</span>
    <span class="k">return</span> <span class="n">final_result</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.Graph.run_sync" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">run_sync</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="nf">run_sync</span><span class="p">(</span>
    <span class="n">start_node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">state</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.graph.GraphRunResult" href="#pydantic_graph.graph.GraphRunResult">GraphRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Synchronously run the graph.</p>
<p>This is a convenience method that wraps <a class="autorefs autorefs-internal" href="#pydantic_graph.graph.Graph.run"><code>self.run</code></a> with <code>loop.run_until_complete(...)</code>.
You therefore can't use this method inside async code or if there's an active event loop.</p>


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
                <code>start_node</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>the first node to run, since the graph definition doesn't define the entry point in the graph,
you need to provide the starting node.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>state</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The initial state of the graph.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>deps</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The dependencies of the graph.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>persistence</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>State persistence interface, defaults to
<a class="autorefs autorefs-internal" href="../persistence/#pydantic_graph.persistence.in_mem.SimpleStatePersistence"><code>SimpleStatePersistence</code></a> if <code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to infer the graph name from the calling frame.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
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
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.graph.GraphRunResult" href="#pydantic_graph.graph.GraphRunResult">GraphRunResult</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The result type from ending the run and the history of the run.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">176</span>
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
<span class="normal">207</span></pre></div></td><td class="code"><div><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">run_sync</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">start_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n">DepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">GraphRunResult</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Synchronously run the graph.</span>

<span class="sd">    This is a convenience method that wraps [`self.run`][pydantic_graph.Graph.run] with `loop.run_until_complete(...)`.</span>
<span class="sd">    You therefore can't use this method inside async code or if there's an active event loop.</span>

<span class="sd">    Args:</span>
<span class="sd">        start_node: the first node to run, since the graph definition doesn't define the entry point in the graph,</span>
<span class="sd">            you need to provide the starting node.</span>
<span class="sd">        state: The initial state of the graph.</span>
<span class="sd">        deps: The dependencies of the graph.</span>
<span class="sd">        persistence: State persistence interface, defaults to</span>
<span class="sd">            [`SimpleStatePersistence`][pydantic_graph.SimpleStatePersistence] if `None`.</span>
<span class="sd">        infer_name: Whether to infer the graph name from the calling frame.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The result type from ending the run and the history of the run.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>

    <span class="k">return</span> <span class="n">_utils</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">start_node</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span> <span class="n">persistence</span><span class="o">=</span><span class="n">persistence</span><span class="p">,</span> <span class="n">infer_name</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.Graph.iter" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">iter</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code><span class="nb">iter</span><span class="p">(</span>
    <span class="nf">start_node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">state</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">span</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="contextlib.AbstractContextManager" href="https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager">AbstractContextManager</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.graph.GraphRun" href="#pydantic_graph.graph.GraphRun">GraphRun</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A contextmanager which can be used to iterate over the graph's nodes as they are executed.</p>
<p>This method returns a <code>GraphRun</code> object which can be used to async-iterate over the nodes of this <code>Graph</code> as
they are executed. This is the API to use if you want to record or interact with the nodes as the graph
execution unfolds.</p>
<p>The <code>GraphRun</code> can also be used to manually drive the graph execution by calling
<a class="autorefs autorefs-internal" href="#pydantic_graph.graph.GraphRun.next"><code>GraphRun.next</code></a>.</p>
<p>The <code>GraphRun</code> provides access to the full run history, state, deps, and the final result of the run once
it has completed.</p>
<p>For more details, see the API documentation of <a class="autorefs autorefs-internal" href="#pydantic_graph.graph.GraphRun"><code>GraphRun</code></a>.</p>


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
                <code>start_node</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>the first node to run. Since the graph definition doesn't define the entry point in the graph,
you need to provide the starting node.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>state</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The initial state of the graph.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>deps</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The dependencies of the graph.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>persistence</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>State persistence interface, defaults to
<a class="autorefs autorefs-internal" href="../persistence/#pydantic_graph.persistence.in_mem.SimpleStatePersistence"><code>SimpleStatePersistence</code></a> if <code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>span</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="contextlib.AbstractContextManager" href="https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager">AbstractContextManager</a>[<a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The span to use for the graph run. If not provided, a new span will be created.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to infer the graph name from the calling frame.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>
        <p>Returns: A GraphRun that can be async iterated over to drive the graph to completion.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">209</span>
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
<span class="normal">263</span></pre></div></td><td class="code"><div><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code tabindex="0"><span class="nd">@asynccontextmanager</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">iter</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">start_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n">DepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">span</span><span class="p">:</span> <span class="n">AbstractContextManager</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">GraphRun</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""A contextmanager which can be used to iterate over the graph's nodes as they are executed.</span>

<span class="sd">    This method returns a `GraphRun` object which can be used to async-iterate over the nodes of this `Graph` as</span>
<span class="sd">    they are executed. This is the API to use if you want to record or interact with the nodes as the graph</span>
<span class="sd">    execution unfolds.</span>

<span class="sd">    The `GraphRun` can also be used to manually drive the graph execution by calling</span>
<span class="sd">    [`GraphRun.next`][pydantic_graph.graph.GraphRun.next].</span>

<span class="sd">    The `GraphRun` provides access to the full run history, state, deps, and the final result of the run once</span>
<span class="sd">    it has completed.</span>

<span class="sd">    For more details, see the API documentation of [`GraphRun`][pydantic_graph.graph.GraphRun].</span>

<span class="sd">    Args:</span>
<span class="sd">        start_node: the first node to run. Since the graph definition doesn't define the entry point in the graph,</span>
<span class="sd">            you need to provide the starting node.</span>
<span class="sd">        state: The initial state of the graph.</span>
<span class="sd">        deps: The dependencies of the graph.</span>
<span class="sd">        persistence: State persistence interface, defaults to</span>
<span class="sd">            [`SimpleStatePersistence`][pydantic_graph.SimpleStatePersistence] if `None`.</span>
<span class="sd">        span: The span to use for the graph run. If not provided, a new span will be created.</span>
<span class="sd">        infer_name: Whether to infer the graph name from the calling frame.</span>

<span class="sd">    Returns: A GraphRun that can be async iterated over to drive the graph to completion.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># f_back because `asynccontextmanager` adds one frame</span>
        <span class="k">if</span> <span class="n">frame</span> <span class="o">:=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">():</span>  <span class="c1"># pragma: no branch</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">frame</span><span class="o">.</span><span class="n">f_back</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">persistence</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">persistence</span> <span class="o">=</span> <span class="n">SimpleStatePersistence</span><span class="p">()</span>
    <span class="n">persistence</span><span class="o">.</span><span class="n">set_graph_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">auto_instrument</span> <span class="ow">and</span> <span class="n">span</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">span</span> <span class="o">=</span> <span class="n">logfire_api</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'run graph </span><span class="si">{graph.name}</span><span class="s1">'</span><span class="p">,</span> <span class="n">graph</span><span class="o">=</span><span class="bp">self</span><span class="p">)</span>

    <span class="k">with</span> <span class="n">ExitStack</span><span class="p">()</span> <span class="k">as</span> <span class="n">stack</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">span</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">stack</span><span class="o">.</span><span class="n">enter_context</span><span class="p">(</span><span class="n">span</span><span class="p">)</span>
        <span class="k">yield</span> <span class="n">GraphRun</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">](</span>
            <span class="n">graph</span><span class="o">=</span><span class="bp">self</span><span class="p">,</span> <span class="n">start_node</span><span class="o">=</span><span class="n">start_node</span><span class="p">,</span> <span class="n">persistence</span><span class="o">=</span><span class="n">persistence</span><span class="p">,</span> <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">deps</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.Graph.iter_from_persistence" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">iter_from_persistence</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="nf">iter_from_persistence</span><span class="p">(</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">span</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="contextlib.AbstractContextManager" href="https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager">AbstractContextManager</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.graph.GraphRun" href="#pydantic_graph.graph.GraphRun">GraphRun</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A contextmanager to iterate over the graph's nodes as they are executed, created from a persistence object.</p>
<p>This method has similar functionality to <a class="autorefs autorefs-internal" href="#pydantic_graph.graph.Graph.iter"><code>iter</code></a>,
but instead of passing the node to run, it will restore the node and state from state persistence.</p>


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
                <code>persistence</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The state persistence interface to use.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>deps</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The dependencies of the graph.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>span</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="contextlib.AbstractContextManager" href="https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager">AbstractContextManager</a>[<a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The span to use for the graph run. If not provided, a new span will be created.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to infer the graph name from the calling frame.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>
        <p>Returns: A GraphRun that can be async iterated over to drive the graph to completion.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">265</span>
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
<span class="normal">313</span></pre></div></td><td class="code"><div><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code tabindex="0"><span class="nd">@asynccontextmanager</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">iter_from_persistence</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n">DepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">span</span><span class="p">:</span> <span class="n">AbstractContextManager</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">GraphRun</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]:</span>
<span class="w">    </span><span class="sd">"""A contextmanager to iterate over the graph's nodes as they are executed, created from a persistence object.</span>

<span class="sd">    This method has similar functionality to [`iter`][pydantic_graph.graph.Graph.iter],</span>
<span class="sd">    but instead of passing the node to run, it will restore the node and state from state persistence.</span>

<span class="sd">    Args:</span>
<span class="sd">        persistence: The state persistence interface to use.</span>
<span class="sd">        deps: The dependencies of the graph.</span>
<span class="sd">        span: The span to use for the graph run. If not provided, a new span will be created.</span>
<span class="sd">        infer_name: Whether to infer the graph name from the calling frame.</span>

<span class="sd">    Returns: A GraphRun that can be async iterated over to drive the graph to completion.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># f_back because `asynccontextmanager` adds one frame</span>
        <span class="k">if</span> <span class="n">frame</span> <span class="o">:=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">():</span>  <span class="c1"># pragma: no branch</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">frame</span><span class="o">.</span><span class="n">f_back</span><span class="p">)</span>

    <span class="n">persistence</span><span class="o">.</span><span class="n">set_graph_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>

    <span class="n">snapshot</span> <span class="o">=</span> <span class="k">await</span> <span class="n">persistence</span><span class="o">.</span><span class="n">load_next</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">snapshot</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">GraphRuntimeError</span><span class="p">(</span><span class="s1">'Unable to restore snapshot from state persistence.'</span><span class="p">)</span>

    <span class="n">snapshot</span><span class="o">.</span><span class="n">node</span><span class="o">.</span><span class="n">set_snapshot_id</span><span class="p">(</span><span class="n">snapshot</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>

    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">auto_instrument</span> <span class="ow">and</span> <span class="n">span</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">span</span> <span class="o">=</span> <span class="n">logfire_api</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'run graph </span><span class="si">{graph.name}</span><span class="s1">'</span><span class="p">,</span> <span class="n">graph</span><span class="o">=</span><span class="bp">self</span><span class="p">)</span>

    <span class="k">with</span> <span class="n">ExitStack</span><span class="p">()</span> <span class="k">as</span> <span class="n">stack</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">span</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">stack</span><span class="o">.</span><span class="n">enter_context</span><span class="p">(</span><span class="n">span</span><span class="p">)</span>
        <span class="k">yield</span> <span class="n">GraphRun</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">](</span>
            <span class="n">graph</span><span class="o">=</span><span class="bp">self</span><span class="p">,</span>
            <span class="n">start_node</span><span class="o">=</span><span class="n">snapshot</span><span class="o">.</span><span class="n">node</span><span class="p">,</span>
            <span class="n">persistence</span><span class="o">=</span><span class="n">persistence</span><span class="p">,</span>
            <span class="n">state</span><span class="o">=</span><span class="n">snapshot</span><span class="o">.</span><span class="n">state</span><span class="p">,</span>
            <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span>
            <span class="n">snapshot_id</span><span class="o">=</span><span class="n">snapshot</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.Graph.initialize" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">initialize</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="nf">initialize</span><span class="p">(</span>
    <span class="n">node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">],</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">state</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Initialize a new graph run in persistence without running it.</p>
<p>This is useful if you want to set up a graph run to be run later, e.g. via
<a class="autorefs autorefs-internal" href="#pydantic_graph.graph.Graph.iter_from_persistence"><code>iter_from_persistence</code></a>.</p>


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
                <code>node</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The node to run first.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>persistence</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>State persistence interface.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>state</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The start state of the graph.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to infer the graph name from the calling frame.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">315</span>
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
<span class="normal">338</span></pre></div></td><td class="code"><div><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">initialize</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize a new graph run in persistence without running it.</span>

<span class="sd">    This is useful if you want to set up a graph run to be run later, e.g. via</span>
<span class="sd">    [`iter_from_persistence`][pydantic_graph.graph.Graph.iter_from_persistence].</span>

<span class="sd">    Args:</span>
<span class="sd">        node: The node to run first.</span>
<span class="sd">        persistence: State persistence interface.</span>
<span class="sd">        state: The start state of the graph.</span>
<span class="sd">        infer_name: Whether to infer the graph name from the calling frame.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>

    <span class="n">persistence</span><span class="o">.</span><span class="n">set_graph_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
    <span class="k">await</span> <span class="n">persistence</span><span class="o">.</span><span class="n">snapshot_node</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.Graph.next" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">next</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="nb">next</span><span class="p">(</span>
    <span class="nf">node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">],</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">state</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.End" href="../nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Run a node in the graph and return the next node to run.</p>


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
                <code>node</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The node to run.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>persistence</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>State persistence interface, defaults to
<a class="autorefs autorefs-internal" href="../persistence/#pydantic_graph.persistence.in_mem.SimpleStatePersistence"><code>SimpleStatePersistence</code></a> if <code>None</code>.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>state</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The current state of the graph.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>deps</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The dependencies of the graph.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to infer the graph name from the calling frame.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
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
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>] | <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.End" href="../nodes/#pydantic_graph.nodes.End">End</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The next node to run or <a class="autorefs autorefs-internal" href="../nodes/#pydantic_graph.nodes.End"><code>End</code></a> if the graph has finished.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">340</span>
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
<span class="normal">374</span></pre></div></td><td class="code"><div><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code><span class="nd">@deprecated</span><span class="p">(</span><span class="s1">'`next` is deprecated, use `async with graph.iter(...) as run:  run.next()` instead'</span><span class="p">)</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">next</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n">DepsT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Run a node in the graph and return the next node to run.</span>

<span class="sd">    Args:</span>
<span class="sd">        node: The node to run.</span>
<span class="sd">        persistence: State persistence interface, defaults to</span>
<span class="sd">            [`SimpleStatePersistence`][pydantic_graph.SimpleStatePersistence] if `None`.</span>
<span class="sd">        state: The current state of the graph.</span>
<span class="sd">        deps: The dependencies of the graph.</span>
<span class="sd">        infer_name: Whether to infer the graph name from the calling frame.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The next node to run or [`End`][pydantic_graph.nodes.End] if the graph has finished.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>

    <span class="n">persistence</span><span class="o">.</span><span class="n">set_graph_types</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
    <span class="n">run</span> <span class="o">=</span> <span class="n">GraphRun</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">](</span>
        <span class="n">graph</span><span class="o">=</span><span class="bp">self</span><span class="p">,</span>
        <span class="n">start_node</span><span class="o">=</span><span class="n">node</span><span class="p">,</span>
        <span class="n">persistence</span><span class="o">=</span><span class="n">persistence</span><span class="p">,</span>
        <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">,</span>
        <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">return</span> <span class="k">await</span> <span class="n">run</span><span class="o">.</span><span class="n">next</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.Graph.mermaid_code" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">mermaid_code</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="nf">mermaid_code</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">start_node</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="../mermaid/#pydantic_graph.mermaid.NodeIdent">NodeIdent</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="../mermaid/#pydantic_graph.mermaid.NodeIdent">NodeIdent</a></span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">title</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.Literal" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Literal">Literal</a></span><span class="p">[</span><span class="kc">False</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">edge_labels</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">notes</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">highlighted_nodes</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="../mermaid/#pydantic_graph.mermaid.NodeIdent">NodeIdent</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="../mermaid/#pydantic_graph.mermaid.NodeIdent">NodeIdent</a></span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">highlight_css</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS" href="../mermaid/#pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS">DEFAULT_HIGHLIGHT_CSS</a></span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">direction</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.StateDiagramDirection" href="../mermaid/#pydantic_graph.mermaid.StateDiagramDirection">StateDiagramDirection</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Generate a diagram representing the graph as <a href="https://mermaid.js.org/">mermaid</a> diagram.</p>
<p>This method calls <a class="autorefs autorefs-internal" href="../mermaid/#pydantic_graph.mermaid.generate_code"><code>pydantic_graph.mermaid.generate_code</code></a>.</p>


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
                <code>start_node</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="../mermaid/#pydantic_graph.mermaid.NodeIdent">NodeIdent</a>] | <a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="../mermaid/#pydantic_graph.mermaid.NodeIdent">NodeIdent</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The node or nodes which can start the graph.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>title</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None | <a class="autorefs autorefs-external" title="typing_extensions.Literal" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Literal">Literal</a>[False]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The title of the diagram, use <code>False</code> to not include a title.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>edge_labels</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to include edge labels.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>notes</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to include notes on each node.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>highlighted_nodes</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="../mermaid/#pydantic_graph.mermaid.NodeIdent">NodeIdent</a>] | <a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="../mermaid/#pydantic_graph.mermaid.NodeIdent">NodeIdent</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional node or nodes to highlight.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>highlight_css</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The CSS to use for highlighting nodes.</p>
              </div>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS" href="../mermaid/#pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS">DEFAULT_HIGHLIGHT_CSS</a></code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to infer the graph name from the calling frame.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>direction</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.StateDiagramDirection" href="../mermaid/#pydantic_graph.mermaid.StateDiagramDirection">StateDiagramDirection</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The direction of flow.</p>
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
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The mermaid code for the graph, which can then be rendered as a diagram.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>
        <p>Here's an example of generating a diagram for the graph from <a class="autorefs autorefs-internal" href="#pydantic_graph.graph.Graph">above</a>:</p>
<div class="language-py highlight"><span class="filename">mermaid_never_42.py</span><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">never_42</span><span class="w"> </span><span class="kn">import</span> <span class="n">Increment</span><span class="p">,</span> <span class="n">never_42_graph</span>

<span class="nb">print</span><span class="p">(</span><span class="n">never_42_graph</span><span class="o">.</span><span class="n">mermaid_code</span><span class="p">(</span><span class="n">start_node</span><span class="o">=</span><span class="n">Increment</span><span class="p">))</span>
<span class="sd">'''</span>
<span class="sd">---</span>
<span class="sd">title: never_42_graph</span>
<span class="sd">---</span>
<span class="sd">stateDiagram-v2</span>
<span class="sd">  [*] --&gt; Increment</span>
<span class="sd">  Increment --&gt; Check42</span>
<span class="sd">  Check42 --&gt; Increment</span>
<span class="sd">  Check42 --&gt; [*]</span>
<span class="sd">'''</span>
</code></pre></div>
<p>The rendered diagram will look like this:</p>
<div class="mermaid"></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">376</span>
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
<span class="normal">449</span></pre></div></td><td class="code"><div><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">mermaid_code</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">start_node</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">mermaid</span><span class="o">.</span><span class="n">NodeIdent</span><span class="p">]</span> <span class="o">|</span> <span class="n">mermaid</span><span class="o">.</span><span class="n">NodeIdent</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">title</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">|</span> <span class="n">typing_extensions</span><span class="o">.</span><span class="n">Literal</span><span class="p">[</span><span class="kc">False</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">edge_labels</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">notes</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">highlighted_nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">mermaid</span><span class="o">.</span><span class="n">NodeIdent</span><span class="p">]</span> <span class="o">|</span> <span class="n">mermaid</span><span class="o">.</span><span class="n">NodeIdent</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">highlight_css</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">mermaid</span><span class="o">.</span><span class="n">DEFAULT_HIGHLIGHT_CSS</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">direction</span><span class="p">:</span> <span class="n">mermaid</span><span class="o">.</span><span class="n">StateDiagramDirection</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generate a diagram representing the graph as [mermaid](https://mermaid.js.org/) diagram.</span>

<span class="sd">    This method calls [`pydantic_graph.mermaid.generate_code`][pydantic_graph.mermaid.generate_code].</span>

<span class="sd">    Args:</span>
<span class="sd">        start_node: The node or nodes which can start the graph.</span>
<span class="sd">        title: The title of the diagram, use `False` to not include a title.</span>
<span class="sd">        edge_labels: Whether to include edge labels.</span>
<span class="sd">        notes: Whether to include notes on each node.</span>
<span class="sd">        highlighted_nodes: Optional node or nodes to highlight.</span>
<span class="sd">        highlight_css: The CSS to use for highlighting nodes.</span>
<span class="sd">        infer_name: Whether to infer the graph name from the calling frame.</span>
<span class="sd">        direction: The direction of flow.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The mermaid code for the graph, which can then be rendered as a diagram.</span>

<span class="sd">    Here's an example of generating a diagram for the graph from [above][pydantic_graph.graph.Graph]:</span>

<span class="sd">    ```py {title="mermaid_never_42.py" py="3.10"}</span>
<span class="sd">    from never_42 import Increment, never_42_graph</span>

<span class="sd">    print(never_42_graph.mermaid_code(start_node=Increment))</span>
<span class="sd">    '''</span>
<span class="sd">    ---</span>
<span class="sd">    title: never_42_graph</span>
<span class="sd">    ---</span>
<span class="sd">    stateDiagram-v2</span>
<span class="sd">      [*] --&gt; Increment</span>
<span class="sd">      Increment --&gt; Check42</span>
<span class="sd">      Check42 --&gt; Increment</span>
<span class="sd">      Check42 --&gt; [*]</span>
<span class="sd">    '''</span>
<span class="sd">    ```</span>

<span class="sd">    The rendered diagram will look like this:</span>

<span class="sd">    ```mermaid</span>
<span class="sd">    ---</span>
<span class="sd">    title: never_42_graph</span>
<span class="sd">    ---</span>
<span class="sd">    stateDiagram-v2</span>
<span class="sd">      [*] --&gt; Increment</span>
<span class="sd">      Increment --&gt; Check42</span>
<span class="sd">      Check42 --&gt; Increment</span>
<span class="sd">      Check42 --&gt; [*]</span>
<span class="sd">    ```</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
    <span class="k">if</span> <span class="n">title</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">:</span>
        <span class="n">title</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span>
    <span class="k">return</span> <span class="n">mermaid</span><span class="o">.</span><span class="n">generate_code</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">start_node</span><span class="o">=</span><span class="n">start_node</span><span class="p">,</span>
        <span class="n">highlighted_nodes</span><span class="o">=</span><span class="n">highlighted_nodes</span><span class="p">,</span>
        <span class="n">highlight_css</span><span class="o">=</span><span class="n">highlight_css</span><span class="p">,</span>
        <span class="n">title</span><span class="o">=</span><span class="n">title</span> <span class="ow">or</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">edge_labels</span><span class="o">=</span><span class="n">edge_labels</span><span class="p">,</span>
        <span class="n">notes</span><span class="o">=</span><span class="n">notes</span><span class="p">,</span>
        <span class="n">direction</span><span class="o">=</span><span class="n">direction</span><span class="p">,</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.Graph.mermaid_image" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">mermaid_image</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="nf">mermaid_image</span><span class="p">(</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.Unpack" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack">Unpack</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.MermaidConfig" href="../mermaid/#pydantic_graph.mermaid.MermaidConfig">MermaidConfig</a></span><span class="p">]</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Generate a diagram representing the graph as an image.</p>
<p>The format and diagram can be customized using <code>kwargs</code>,
see <a class="autorefs autorefs-internal" href="../mermaid/#pydantic_graph.mermaid.MermaidConfig"><code>pydantic_graph.mermaid.MermaidConfig</code></a>.</p>
<div class="admonition note">
<p class="admonition-title">Uses external service</p>
<p>This method makes a request to <a href="https://mermaid.ink">mermaid.ink</a> to render the image, <code>mermaid.ink</code>
is a free service not affiliated with Pydantic.</p>
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
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to infer the graph name from the calling frame.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing_extensions.Unpack" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack">Unpack</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.MermaidConfig" href="../mermaid/#pydantic_graph.mermaid.MermaidConfig">MermaidConfig</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Additional arguments to pass to <code>mermaid.request_image</code>.</p>
              </div>
            </td>
            <td>
                  <code>{}</code>
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
                <p>The image bytes.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">451</span>
<span class="normal">452</span>
<span class="normal">453</span>
<span class="normal">454</span>
<span class="normal">455</span>
<span class="normal">456</span>
<span class="normal">457</span>
<span class="normal">458</span>
<span class="normal">459</span>
<span class="normal">460</span>
<span class="normal">461</span>
<span class="normal">462</span>
<span class="normal">463</span>
<span class="normal">464</span>
<span class="normal">465</span>
<span class="normal">466</span>
<span class="normal">467</span>
<span class="normal">468</span>
<span class="normal">469</span>
<span class="normal">470</span>
<span class="normal">471</span>
<span class="normal">472</span>
<span class="normal">473</span>
<span class="normal">474</span></pre></div></td><td class="code"><div><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">mermaid_image</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">typing_extensions</span><span class="o">.</span><span class="n">Unpack</span><span class="p">[</span><span class="n">mermaid</span><span class="o">.</span><span class="n">MermaidConfig</span><span class="p">]</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generate a diagram representing the graph as an image.</span>

<span class="sd">    The format and diagram can be customized using `kwargs`,</span>
<span class="sd">    see [`pydantic_graph.mermaid.MermaidConfig`][pydantic_graph.mermaid.MermaidConfig].</span>

<span class="sd">    !!! note "Uses external service"</span>
<span class="sd">        This method makes a request to [mermaid.ink](https://mermaid.ink) to render the image, `mermaid.ink`</span>
<span class="sd">        is a free service not affiliated with Pydantic.</span>

<span class="sd">    Args:</span>
<span class="sd">        infer_name: Whether to infer the graph name from the calling frame.</span>
<span class="sd">        **kwargs: Additional arguments to pass to `mermaid.request_image`.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The image bytes.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
    <span class="k">if</span> <span class="s1">'title'</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">kwargs</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">:</span>
        <span class="n">kwargs</span><span class="p">[</span><span class="s1">'title'</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span>
    <span class="k">return</span> <span class="n">mermaid</span><span class="o">.</span><span class="n">request_image</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.Graph.mermaid_save" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">mermaid_save</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="nf">mermaid_save</span><span class="p">(</span>
    <span class="n">path</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">infer_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.Unpack" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack">Unpack</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.MermaidConfig" href="../mermaid/#pydantic_graph.mermaid.MermaidConfig">MermaidConfig</a></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Generate a diagram representing the graph and save it as an image.</p>
<p>The format and diagram can be customized using <code>kwargs</code>,
see <a class="autorefs autorefs-internal" href="../mermaid/#pydantic_graph.mermaid.MermaidConfig"><code>pydantic_graph.mermaid.MermaidConfig</code></a>.</p>
<div class="admonition note">
<p class="admonition-title">Uses external service</p>
<p>This method makes a request to <a href="https://mermaid.ink">mermaid.ink</a> to render the image, <code>mermaid.ink</code>
is a free service not affiliated with Pydantic.</p>
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
                <code>path</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The path to save the image to.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>infer_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to infer the graph name from the calling frame.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing_extensions.Unpack" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack">Unpack</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.MermaidConfig" href="../mermaid/#pydantic_graph.mermaid.MermaidConfig">MermaidConfig</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Additional arguments to pass to <code>mermaid.save_image</code>.</p>
              </div>
            </td>
            <td>
                  <code>{}</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">476</span>
<span class="normal">477</span>
<span class="normal">478</span>
<span class="normal">479</span>
<span class="normal">480</span>
<span class="normal">481</span>
<span class="normal">482</span>
<span class="normal">483</span>
<span class="normal">484</span>
<span class="normal">485</span>
<span class="normal">486</span>
<span class="normal">487</span>
<span class="normal">488</span>
<span class="normal">489</span>
<span class="normal">490</span>
<span class="normal">491</span>
<span class="normal">492</span>
<span class="normal">493</span>
<span class="normal">494</span>
<span class="normal">495</span>
<span class="normal">496</span>
<span class="normal">497</span></pre></div></td><td class="code"><div><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">mermaid_save</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span><span class="p">,</span> <span class="o">/</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">infer_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">typing_extensions</span><span class="o">.</span><span class="n">Unpack</span><span class="p">[</span><span class="n">mermaid</span><span class="o">.</span><span class="n">MermaidConfig</span><span class="p">]</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generate a diagram representing the graph and save it as an image.</span>

<span class="sd">    The format and diagram can be customized using `kwargs`,</span>
<span class="sd">    see [`pydantic_graph.mermaid.MermaidConfig`][pydantic_graph.mermaid.MermaidConfig].</span>

<span class="sd">    !!! note "Uses external service"</span>
<span class="sd">        This method makes a request to [mermaid.ink](https://mermaid.ink) to render the image, `mermaid.ink`</span>
<span class="sd">        is a free service not affiliated with Pydantic.</span>

<span class="sd">    Args:</span>
<span class="sd">        path: The path to save the image to.</span>
<span class="sd">        infer_name: Whether to infer the graph name from the calling frame.</span>
<span class="sd">        **kwargs: Additional arguments to pass to `mermaid.save_image`.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">infer_name</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_infer_name</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span>
    <span class="k">if</span> <span class="s1">'title'</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">kwargs</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">:</span>
        <span class="n">kwargs</span><span class="p">[</span><span class="s1">'title'</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span>
    <span class="n">mermaid</span><span class="o">.</span><span class="n">save_image</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.Graph.get_nodes" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">get_nodes</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code><span class="nf">get_nodes</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">(</span>
    <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]]]</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the nodes in the graph.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">499</span>
<span class="normal">500</span>
<span class="normal">501</span></pre></div></td><td class="code"><div><pre id="__code_25"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_25 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">get_nodes</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]]]:</span>
<span class="w">    </span><span class="sd">"""Get the nodes in the graph."""</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">node_def</span><span class="o">.</span><span class="n">node</span> <span class="k">for</span> <span class="n">node_def</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">node_defs</span><span class="o">.</span><span class="n">values</span><span class="p">()]</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>








  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_graph.graph.GraphRun" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">GraphRun</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code></p>


        <p>A stateful, async-iterable run of a <a class="autorefs autorefs-internal" href="#pydantic_graph.graph.Graph"><code>Graph</code></a>.</p>
<p>You typically get a <code>GraphRun</code> instance from calling
<code>async with [my_graph.iter(...)][pydantic_graph.graph.Graph.iter] as graph_run:</code>. That gives you the ability to iterate
through nodes as they run, either by <code>async for</code> iteration or by repeatedly calling <code>.next(...)</code>.</p>
<p>Here's an example of iterating over the graph from <a class="autorefs autorefs-internal" href="#pydantic_graph.graph.Graph">above</a>:
</p><div class="language-py highlight"><span class="filename">iter_never_42.py</span><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">copy</span><span class="w"> </span><span class="kn">import</span> <span class="n">deepcopy</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">never_42</span><span class="w"> </span><span class="kn">import</span> <span class="n">Increment</span><span class="p">,</span> <span class="n">MyState</span><span class="p">,</span> <span class="n">never_42_graph</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">state</span> <span class="o">=</span> <span class="n">MyState</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">never_42_graph</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="n">Increment</span><span class="p">(),</span> <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">)</span> <span class="k">as</span> <span class="n">graph_run</span><span class="p">:</span>
        <span class="n">node_states</span> <span class="o">=</span> <span class="p">[(</span><span class="n">graph_run</span><span class="o">.</span><span class="n">next_node</span><span class="p">,</span> <span class="n">deepcopy</span><span class="p">(</span><span class="n">graph_run</span><span class="o">.</span><span class="n">state</span><span class="p">))]</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">graph_run</span><span class="p">:</span>
            <span class="n">node_states</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">node</span><span class="p">,</span> <span class="n">deepcopy</span><span class="p">(</span><span class="n">graph_run</span><span class="o">.</span><span class="n">state</span><span class="p">)))</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">node_states</span><span class="p">)</span>
<span class="w">        </span><span class="sd">'''</span>
<span class="sd">        [</span>
<span class="sd">            (Increment(), MyState(number=1)),</span>
<span class="sd">            (Check42(), MyState(number=2)),</span>
<span class="sd">            (End(data=2), MyState(number=2)),</span>
<span class="sd">        ]</span>
<span class="sd">        '''</span>

    <span class="n">state</span> <span class="o">=</span> <span class="n">MyState</span><span class="p">(</span><span class="mi">41</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">never_42_graph</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="n">Increment</span><span class="p">(),</span> <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">)</span> <span class="k">as</span> <span class="n">graph_run</span><span class="p">:</span>
        <span class="n">node_states</span> <span class="o">=</span> <span class="p">[(</span><span class="n">graph_run</span><span class="o">.</span><span class="n">next_node</span><span class="p">,</span> <span class="n">deepcopy</span><span class="p">(</span><span class="n">graph_run</span><span class="o">.</span><span class="n">state</span><span class="p">))]</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">node</span> <span class="ow">in</span> <span class="n">graph_run</span><span class="p">:</span>
            <span class="n">node_states</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">node</span><span class="p">,</span> <span class="n">deepcopy</span><span class="p">(</span><span class="n">graph_run</span><span class="o">.</span><span class="n">state</span><span class="p">)))</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">node_states</span><span class="p">)</span>
<span class="w">        </span><span class="sd">'''</span>
<span class="sd">        [</span>
<span class="sd">            (Increment(), MyState(number=41)),</span>
<span class="sd">            (Check42(), MyState(number=42)),</span>
<span class="sd">            (Increment(), MyState(number=42)),</span>
<span class="sd">            (Check42(), MyState(number=43)),</span>
<span class="sd">            (End(data=43), MyState(number=43)),</span>
<span class="sd">        ]</span>
<span class="sd">        '''</span>
</code></pre></div><p></p>
<p>See the <a class="autorefs autorefs-internal" href="#pydantic_graph.graph.GraphRun.next"><code>GraphRun.next</code> documentation</a> for an example of how to manually
drive the graph run.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">589</span>
<span class="normal">590</span>
<span class="normal">591</span>
<span class="normal">592</span>
<span class="normal">593</span>
<span class="normal">594</span>
<span class="normal">595</span>
<span class="normal">596</span>
<span class="normal">597</span>
<span class="normal">598</span>
<span class="normal">599</span>
<span class="normal">600</span>
<span class="normal">601</span>
<span class="normal">602</span>
<span class="normal">603</span>
<span class="normal">604</span>
<span class="normal">605</span>
<span class="normal">606</span>
<span class="normal">607</span>
<span class="normal">608</span>
<span class="normal">609</span>
<span class="normal">610</span>
<span class="normal">611</span>
<span class="normal">612</span>
<span class="normal">613</span>
<span class="normal">614</span>
<span class="normal">615</span>
<span class="normal">616</span>
<span class="normal">617</span>
<span class="normal">618</span>
<span class="normal">619</span>
<span class="normal">620</span>
<span class="normal">621</span>
<span class="normal">622</span>
<span class="normal">623</span>
<span class="normal">624</span>
<span class="normal">625</span>
<span class="normal">626</span>
<span class="normal">627</span>
<span class="normal">628</span>
<span class="normal">629</span>
<span class="normal">630</span>
<span class="normal">631</span>
<span class="normal">632</span>
<span class="normal">633</span>
<span class="normal">634</span>
<span class="normal">635</span>
<span class="normal">636</span>
<span class="normal">637</span>
<span class="normal">638</span>
<span class="normal">639</span>
<span class="normal">640</span>
<span class="normal">641</span>
<span class="normal">642</span>
<span class="normal">643</span>
<span class="normal">644</span>
<span class="normal">645</span>
<span class="normal">646</span>
<span class="normal">647</span>
<span class="normal">648</span>
<span class="normal">649</span>
<span class="normal">650</span>
<span class="normal">651</span>
<span class="normal">652</span>
<span class="normal">653</span>
<span class="normal">654</span>
<span class="normal">655</span>
<span class="normal">656</span>
<span class="normal">657</span>
<span class="normal">658</span>
<span class="normal">659</span>
<span class="normal">660</span>
<span class="normal">661</span>
<span class="normal">662</span>
<span class="normal">663</span>
<span class="normal">664</span>
<span class="normal">665</span>
<span class="normal">666</span>
<span class="normal">667</span>
<span class="normal">668</span>
<span class="normal">669</span>
<span class="normal">670</span>
<span class="normal">671</span>
<span class="normal">672</span>
<span class="normal">673</span>
<span class="normal">674</span>
<span class="normal">675</span>
<span class="normal">676</span>
<span class="normal">677</span>
<span class="normal">678</span>
<span class="normal">679</span>
<span class="normal">680</span>
<span class="normal">681</span>
<span class="normal">682</span>
<span class="normal">683</span>
<span class="normal">684</span>
<span class="normal">685</span>
<span class="normal">686</span>
<span class="normal">687</span>
<span class="normal">688</span>
<span class="normal">689</span>
<span class="normal">690</span>
<span class="normal">691</span>
<span class="normal">692</span>
<span class="normal">693</span>
<span class="normal">694</span>
<span class="normal">695</span>
<span class="normal">696</span>
<span class="normal">697</span>
<span class="normal">698</span>
<span class="normal">699</span>
<span class="normal">700</span>
<span class="normal">701</span>
<span class="normal">702</span>
<span class="normal">703</span>
<span class="normal">704</span>
<span class="normal">705</span>
<span class="normal">706</span>
<span class="normal">707</span>
<span class="normal">708</span>
<span class="normal">709</span>
<span class="normal">710</span>
<span class="normal">711</span>
<span class="normal">712</span>
<span class="normal">713</span>
<span class="normal">714</span>
<span class="normal">715</span>
<span class="normal">716</span>
<span class="normal">717</span>
<span class="normal">718</span>
<span class="normal">719</span>
<span class="normal">720</span>
<span class="normal">721</span>
<span class="normal">722</span>
<span class="normal">723</span>
<span class="normal">724</span>
<span class="normal">725</span>
<span class="normal">726</span>
<span class="normal">727</span>
<span class="normal">728</span>
<span class="normal">729</span>
<span class="normal">730</span>
<span class="normal">731</span>
<span class="normal">732</span>
<span class="normal">733</span>
<span class="normal">734</span>
<span class="normal">735</span>
<span class="normal">736</span>
<span class="normal">737</span>
<span class="normal">738</span>
<span class="normal">739</span>
<span class="normal">740</span>
<span class="normal">741</span>
<span class="normal">742</span>
<span class="normal">743</span>
<span class="normal">744</span>
<span class="normal">745</span>
<span class="normal">746</span>
<span class="normal">747</span>
<span class="normal">748</span>
<span class="normal">749</span>
<span class="normal">750</span>
<span class="normal">751</span>
<span class="normal">752</span>
<span class="normal">753</span>
<span class="normal">754</span>
<span class="normal">755</span>
<span class="normal">756</span>
<span class="normal">757</span>
<span class="normal">758</span>
<span class="normal">759</span>
<span class="normal">760</span>
<span class="normal">761</span>
<span class="normal">762</span>
<span class="normal">763</span>
<span class="normal">764</span>
<span class="normal">765</span>
<span class="normal">766</span>
<span class="normal">767</span>
<span class="normal">768</span>
<span class="normal">769</span>
<span class="normal">770</span>
<span class="normal">771</span>
<span class="normal">772</span>
<span class="normal">773</span>
<span class="normal">774</span>
<span class="normal">775</span>
<span class="normal">776</span>
<span class="normal">777</span>
<span class="normal">778</span>
<span class="normal">779</span>
<span class="normal">780</span>
<span class="normal">781</span>
<span class="normal">782</span>
<span class="normal">783</span>
<span class="normal">784</span>
<span class="normal">785</span></pre></div></td><td class="code"><div><pre id="__code_27"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_27 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">GraphRun</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""A stateful, async-iterable run of a [`Graph`][pydantic_graph.graph.Graph].</span>

<span class="sd">    You typically get a `GraphRun` instance from calling</span>
<span class="sd">    `async with [my_graph.iter(...)][pydantic_graph.graph.Graph.iter] as graph_run:`. That gives you the ability to iterate</span>
<span class="sd">    through nodes as they run, either by `async for` iteration or by repeatedly calling `.next(...)`.</span>

<span class="sd">    Here's an example of iterating over the graph from [above][pydantic_graph.graph.Graph]:</span>
<span class="sd">    ```py {title="iter_never_42.py" noqa="I001" py="3.10"}</span>
<span class="sd">    from copy import deepcopy</span>
<span class="sd">    from never_42 import Increment, MyState, never_42_graph</span>

<span class="sd">    async def main():</span>
<span class="sd">        state = MyState(1)</span>
<span class="sd">        async with never_42_graph.iter(Increment(), state=state) as graph_run:</span>
<span class="sd">            node_states = [(graph_run.next_node, deepcopy(graph_run.state))]</span>
<span class="sd">            async for node in graph_run:</span>
<span class="sd">                node_states.append((node, deepcopy(graph_run.state)))</span>
<span class="sd">            print(node_states)</span>
<span class="sd">            '''</span>
<span class="sd">            [</span>
<span class="sd">                (Increment(), MyState(number=1)),</span>
<span class="sd">                (Check42(), MyState(number=2)),</span>
<span class="sd">                (End(data=2), MyState(number=2)),</span>
<span class="sd">            ]</span>
<span class="sd">            '''</span>

<span class="sd">        state = MyState(41)</span>
<span class="sd">        async with never_42_graph.iter(Increment(), state=state) as graph_run:</span>
<span class="sd">            node_states = [(graph_run.next_node, deepcopy(graph_run.state))]</span>
<span class="sd">            async for node in graph_run:</span>
<span class="sd">                node_states.append((node, deepcopy(graph_run.state)))</span>
<span class="sd">            print(node_states)</span>
<span class="sd">            '''</span>
<span class="sd">            [</span>
<span class="sd">                (Increment(), MyState(number=41)),</span>
<span class="sd">                (Check42(), MyState(number=42)),</span>
<span class="sd">                (Increment(), MyState(number=42)),</span>
<span class="sd">                (Check42(), MyState(number=43)),</span>
<span class="sd">                (End(data=43), MyState(number=43)),</span>
<span class="sd">            ]</span>
<span class="sd">            '''</span>
<span class="sd">    ```</span>

<span class="sd">    See the [`GraphRun.next` documentation][pydantic_graph.graph.GraphRun.next] for an example of how to manually</span>
<span class="sd">    drive the graph run.</span>
<span class="sd">    """</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">graph</span><span class="p">:</span> <span class="n">Graph</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
        <span class="n">start_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
        <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
        <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span>
        <span class="n">deps</span><span class="p">:</span> <span class="n">DepsT</span><span class="p">,</span>
        <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Create a new run for a given graph, starting at the specified node.</span>

<span class="sd">        Typically, you'll use [`Graph.iter`][pydantic_graph.graph.Graph.iter] rather than calling this directly.</span>

<span class="sd">        Args:</span>
<span class="sd">            graph: The [`Graph`][pydantic_graph.graph.Graph] to run.</span>
<span class="sd">            start_node: The node where execution will begin.</span>
<span class="sd">            persistence: State persistence interface.</span>
<span class="sd">            state: A shared state object or primitive (like a counter, dataclass, etc.) that is available</span>
<span class="sd">                to all nodes via `ctx.state`.</span>
<span class="sd">            deps: Optional dependencies that each node can access via `ctx.deps`, e.g. database connections,</span>
<span class="sd">                configuration, or logging clients.</span>
<span class="sd">            snapshot_id: The ID of the snapshot the node came from.</span>
<span class="sd">        """</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">graph</span> <span class="o">=</span> <span class="n">graph</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">persistence</span> <span class="o">=</span> <span class="n">persistence</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_snapshot_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">snapshot_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">state</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">deps</span> <span class="o">=</span> <span class="n">deps</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]</span> <span class="o">=</span> <span class="n">start_node</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">next_node</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""The next node that will be run in the graph.</span>

<span class="sd">        This is the next node that will be used during async iteration, or if a node is not passed to `self.next(...)`.</span>
<span class="sd">        """</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">result</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">GraphRunResult</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The final result of the graph run if the run is completed, otherwise `None`."""</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">,</span> <span class="n">End</span><span class="p">):</span>
            <span class="k">return</span> <span class="kc">None</span>  <span class="c1"># The GraphRun has not finished running</span>
        <span class="k">return</span> <span class="n">GraphRunResult</span><span class="p">(</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="o">.</span><span class="n">data</span><span class="p">,</span>
            <span class="n">state</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="p">,</span>
            <span class="n">persistence</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">persistence</span><span class="p">,</span>
        <span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">next</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Manually drive the graph run by passing in the node you want to run next.</span>

<span class="sd">        This lets you inspect or mutate the node before continuing execution, or skip certain nodes</span>
<span class="sd">        under dynamic conditions. The graph run should stop when you return an [`End`][pydantic_graph.nodes.End] node.</span>

<span class="sd">        Here's an example of using `next` to drive the graph from [above][pydantic_graph.graph.Graph]:</span>
<span class="sd">        ```py {title="next_never_42.py" noqa="I001" py="3.10"}</span>
<span class="sd">        from copy import deepcopy</span>
<span class="sd">        from pydantic_graph import End</span>
<span class="sd">        from never_42 import Increment, MyState, never_42_graph</span>

<span class="sd">        async def main():</span>
<span class="sd">            state = MyState(48)</span>
<span class="sd">            async with never_42_graph.iter(Increment(), state=state) as graph_run:</span>
<span class="sd">                next_node = graph_run.next_node  # start with the first node</span>
<span class="sd">                node_states = [(next_node, deepcopy(graph_run.state))]</span>

<span class="sd">                while not isinstance(next_node, End):</span>
<span class="sd">                    if graph_run.state.number == 50:</span>
<span class="sd">                        graph_run.state.number = 42</span>
<span class="sd">                    next_node = await graph_run.next(next_node)</span>
<span class="sd">                    node_states.append((next_node, deepcopy(graph_run.state)))</span>

<span class="sd">                print(node_states)</span>
<span class="sd">                '''</span>
<span class="sd">                [</span>
<span class="sd">                    (Increment(), MyState(number=48)),</span>
<span class="sd">                    (Check42(), MyState(number=49)),</span>
<span class="sd">                    (End(data=49), MyState(number=49)),</span>
<span class="sd">                ]</span>
<span class="sd">                '''</span>
<span class="sd">        ```</span>

<span class="sd">        Args:</span>
<span class="sd">            node: The node to run next in the graph. If not specified, uses `self.next_node`, which is initialized to</span>
<span class="sd">                the `start_node` of the run and updated each time a new node is returned.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The next node returned by the graph logic, or an [`End`][pydantic_graph.nodes.End] node if</span>
<span class="sd">            the run has completed.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">node</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="c1"># This cast is necessary because self._next_node could be an `End`. You'll get a runtime error if that's</span>
            <span class="c1"># the case, but if it is, the only way to get there would be to have tried calling next manually after</span>
            <span class="c1"># the run finished. Either way, maybe it would be better to not do this cast...</span>
            <span class="n">node</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">)</span>
            <span class="n">node_snapshot_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_snapshot_id</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">node_snapshot_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_snapshot_id</span><span class="p">()</span>

        <span class="k">if</span> <span class="n">node_snapshot_id</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshot_id</span><span class="p">:</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">persistence</span><span class="o">.</span><span class="n">snapshot_node_if_new</span><span class="p">(</span><span class="n">node_snapshot_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_snapshot_id</span> <span class="o">=</span> <span class="n">node_snapshot_id</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">):</span>
            <span class="c1"># While technically this is not compatible with the documented method signature, it's an easy mistake to</span>
            <span class="c1"># make, and we should eagerly provide a more helpful error message than you'd get otherwise.</span>
            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'`next` must be called with a `BaseNode` instance, got </span><span class="si">{</span><span class="n">node</span><span class="si">!r}</span><span class="s1">.'</span><span class="p">)</span>

        <span class="n">node_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_node_id</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">node_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph</span><span class="o">.</span><span class="n">node_defs</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">GraphRuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Node `</span><span class="si">{</span><span class="n">node</span><span class="si">}</span><span class="s1">` is not in the graph.'</span><span class="p">)</span>

        <span class="k">with</span> <span class="n">ExitStack</span><span class="p">()</span> <span class="k">as</span> <span class="n">stack</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph</span><span class="o">.</span><span class="n">auto_instrument</span><span class="p">:</span>
                <span class="n">stack</span><span class="o">.</span><span class="n">enter_context</span><span class="p">(</span><span class="n">_logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'run node </span><span class="si">{node_id}</span><span class="s1">'</span><span class="p">,</span> <span class="n">node_id</span><span class="o">=</span><span class="n">node_id</span><span class="p">,</span> <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">))</span>

            <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">persistence</span><span class="o">.</span><span class="n">record_run</span><span class="p">(</span><span class="n">node_snapshot_id</span><span class="p">):</span>
                <span class="n">ctx</span> <span class="o">=</span> <span class="n">GraphRunContext</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">deps</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span> <span class="o">=</span> <span class="k">await</span> <span class="n">node</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">,</span> <span class="n">End</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_snapshot_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="o">.</span><span class="n">get_snapshot_id</span><span class="p">()</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">persistence</span><span class="o">.</span><span class="n">snapshot_end</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">)</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_snapshot_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="o">.</span><span class="n">get_snapshot_id</span><span class="p">()</span>
            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">persistence</span><span class="o">.</span><span class="n">snapshot_node</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">GraphRuntimeError</span><span class="p">(</span>
                <span class="sa">f</span><span class="s1">'Invalid node return type: `</span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">`. Expected `BaseNode` or `End`.'</span>
            <span class="p">)</span>

        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__aiter__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]]:</span>
        <span class="k">return</span> <span class="bp">self</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="fm">__anext__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Use the last returned node as the input to `Graph.next`."""</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">,</span> <span class="n">End</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">StopAsyncIteration</span>
        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">next</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s1">'&lt;GraphRun graph=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">graph</span><span class="o">.</span><span class="n">name</span><span class="w"> </span><span class="ow">or</span><span class="w"> </span><span class="s2">"[unnamed]"</span><span class="si">}</span><span class="s1">&gt;'</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.GraphRun.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_28"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_28 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">graph</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.graph.Graph" href="#pydantic_graph.graph.Graph">Graph</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">],</span>
    <span class="n">start_node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">],</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">],</span>
    <span class="n">state</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span>
    <span class="n">snapshot_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a new run for a given graph, starting at the specified node.</p>
<p>Typically, you'll use <a class="autorefs autorefs-internal" href="#pydantic_graph.graph.Graph.iter"><code>Graph.iter</code></a> rather than calling this directly.</p>


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
                <code>graph</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.graph.Graph" href="#pydantic_graph.graph.Graph">Graph</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The <a class="autorefs autorefs-internal" href="#pydantic_graph.graph.Graph"><code>Graph</code></a> to run.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>start_node</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The node where execution will begin.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>persistence</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.persistence.BaseStatePersistence" href="../persistence/#pydantic_graph.persistence.BaseStatePersistence">BaseStatePersistence</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>State persistence interface.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>state</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A shared state object or primitive (like a counter, dataclass, etc.) that is available
to all nodes via <code>ctx.state</code>.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>deps</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Optional dependencies that each node can access via <code>ctx.deps</code>, e.g. database connections,
configuration, or logging clients.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>snapshot_id</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The ID of the snapshot the node came from.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">637</span>
<span class="normal">638</span>
<span class="normal">639</span>
<span class="normal">640</span>
<span class="normal">641</span>
<span class="normal">642</span>
<span class="normal">643</span>
<span class="normal">644</span>
<span class="normal">645</span>
<span class="normal">646</span>
<span class="normal">647</span>
<span class="normal">648</span>
<span class="normal">649</span>
<span class="normal">650</span>
<span class="normal">651</span>
<span class="normal">652</span>
<span class="normal">653</span>
<span class="normal">654</span>
<span class="normal">655</span>
<span class="normal">656</span>
<span class="normal">657</span>
<span class="normal">658</span>
<span class="normal">659</span>
<span class="normal">660</span>
<span class="normal">661</span>
<span class="normal">662</span>
<span class="normal">663</span>
<span class="normal">664</span>
<span class="normal">665</span>
<span class="normal">666</span>
<span class="normal">667</span></pre></div></td><td class="code"><div><pre id="__code_29"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_29 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">graph</span><span class="p">:</span> <span class="n">Graph</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
    <span class="n">start_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span>
    <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span><span class="p">,</span>
    <span class="n">deps</span><span class="p">:</span> <span class="n">DepsT</span><span class="p">,</span>
    <span class="n">snapshot_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Create a new run for a given graph, starting at the specified node.</span>

<span class="sd">    Typically, you'll use [`Graph.iter`][pydantic_graph.graph.Graph.iter] rather than calling this directly.</span>

<span class="sd">    Args:</span>
<span class="sd">        graph: The [`Graph`][pydantic_graph.graph.Graph] to run.</span>
<span class="sd">        start_node: The node where execution will begin.</span>
<span class="sd">        persistence: State persistence interface.</span>
<span class="sd">        state: A shared state object or primitive (like a counter, dataclass, etc.) that is available</span>
<span class="sd">            to all nodes via `ctx.state`.</span>
<span class="sd">        deps: Optional dependencies that each node can access via `ctx.deps`, e.g. database connections,</span>
<span class="sd">            configuration, or logging clients.</span>
<span class="sd">        snapshot_id: The ID of the snapshot the node came from.</span>
<span class="sd">    """</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">graph</span> <span class="o">=</span> <span class="n">graph</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">persistence</span> <span class="o">=</span> <span class="n">persistence</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_snapshot_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">snapshot_id</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">state</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">deps</span> <span class="o">=</span> <span class="n">deps</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]</span> <span class="o">=</span> <span class="n">start_node</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.graph.GraphRun.next_node" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">next_node</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_30"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_30 > code"></button><code><span class="n">next_node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.End" href="../nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The next node that will be run in the graph.</p>
<p>This is the next node that will be used during async iteration, or if a node is not passed to <code>self.next(...)</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.graph.GraphRun.result" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">result</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_31"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_31 > code"></button><code><span class="n">result</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.graph.GraphRunResult" href="#pydantic_graph.graph.GraphRunResult">GraphRunResult</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The final result of the graph run if the run is completed, otherwise <code>None</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.GraphRun.next" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">next</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_32"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_32 > code"></button><code><span class="nb">next</span><span class="p">(</span>
    <span class="nf">node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.End" href="../nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Manually drive the graph run by passing in the node you want to run next.</p>
<p>This lets you inspect or mutate the node before continuing execution, or skip certain nodes
under dynamic conditions. The graph run should stop when you return an <a class="autorefs autorefs-internal" href="../nodes/#pydantic_graph.nodes.End"><code>End</code></a> node.</p>
<p>Here's an example of using <code>next</code> to drive the graph from <a class="autorefs autorefs-internal" href="#pydantic_graph.graph.Graph">above</a>:
</p><div class="language-py highlight"><span class="filename">next_never_42.py</span><pre id="__code_33"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_33 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">copy</span><span class="w"> </span><span class="kn">import</span> <span class="n">deepcopy</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_graph</span><span class="w"> </span><span class="kn">import</span> <span class="n">End</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">never_42</span><span class="w"> </span><span class="kn">import</span> <span class="n">Increment</span><span class="p">,</span> <span class="n">MyState</span><span class="p">,</span> <span class="n">never_42_graph</span>

<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="n">state</span> <span class="o">=</span> <span class="n">MyState</span><span class="p">(</span><span class="mi">48</span><span class="p">)</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">never_42_graph</span><span class="o">.</span><span class="n">iter</span><span class="p">(</span><span class="n">Increment</span><span class="p">(),</span> <span class="n">state</span><span class="o">=</span><span class="n">state</span><span class="p">)</span> <span class="k">as</span> <span class="n">graph_run</span><span class="p">:</span>
        <span class="n">next_node</span> <span class="o">=</span> <span class="n">graph_run</span><span class="o">.</span><span class="n">next_node</span>  <span class="c1"># start with the first node</span>
        <span class="n">node_states</span> <span class="o">=</span> <span class="p">[(</span><span class="n">next_node</span><span class="p">,</span> <span class="n">deepcopy</span><span class="p">(</span><span class="n">graph_run</span><span class="o">.</span><span class="n">state</span><span class="p">))]</span>

        <span class="k">while</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">next_node</span><span class="p">,</span> <span class="n">End</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">graph_run</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">number</span> <span class="o">==</span> <span class="mi">50</span><span class="p">:</span>
                <span class="n">graph_run</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">number</span> <span class="o">=</span> <span class="mi">42</span>
            <span class="n">next_node</span> <span class="o">=</span> <span class="k">await</span> <span class="n">graph_run</span><span class="o">.</span><span class="n">next</span><span class="p">(</span><span class="n">next_node</span><span class="p">)</span>
            <span class="n">node_states</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">next_node</span><span class="p">,</span> <span class="n">deepcopy</span><span class="p">(</span><span class="n">graph_run</span><span class="o">.</span><span class="n">state</span><span class="p">)))</span>

        <span class="nb">print</span><span class="p">(</span><span class="n">node_states</span><span class="p">)</span>
<span class="w">        </span><span class="sd">'''</span>
<span class="sd">        [</span>
<span class="sd">            (Increment(), MyState(number=48)),</span>
<span class="sd">            (Check42(), MyState(number=49)),</span>
<span class="sd">            (End(data=49), MyState(number=49)),</span>
<span class="sd">        ]</span>
<span class="sd">        '''</span>
</code></pre></div><p></p>


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
                <code>node</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The node to run next in the graph. If not specified, uses <code>self.next_node</code>, which is initialized to
the <code>start_node</code> of the run and updated each time a new node is returned.</p>
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
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>] | <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.End" href="../nodes/#pydantic_graph.nodes.End">End</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The next node returned by the graph logic, or an <a class="autorefs autorefs-internal" href="../nodes/#pydantic_graph.nodes.End"><code>End</code></a> node if</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>] | <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.End" href="../nodes/#pydantic_graph.nodes.End">End</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>the run has completed.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">688</span>
<span class="normal">689</span>
<span class="normal">690</span>
<span class="normal">691</span>
<span class="normal">692</span>
<span class="normal">693</span>
<span class="normal">694</span>
<span class="normal">695</span>
<span class="normal">696</span>
<span class="normal">697</span>
<span class="normal">698</span>
<span class="normal">699</span>
<span class="normal">700</span>
<span class="normal">701</span>
<span class="normal">702</span>
<span class="normal">703</span>
<span class="normal">704</span>
<span class="normal">705</span>
<span class="normal">706</span>
<span class="normal">707</span>
<span class="normal">708</span>
<span class="normal">709</span>
<span class="normal">710</span>
<span class="normal">711</span>
<span class="normal">712</span>
<span class="normal">713</span>
<span class="normal">714</span>
<span class="normal">715</span>
<span class="normal">716</span>
<span class="normal">717</span>
<span class="normal">718</span>
<span class="normal">719</span>
<span class="normal">720</span>
<span class="normal">721</span>
<span class="normal">722</span>
<span class="normal">723</span>
<span class="normal">724</span>
<span class="normal">725</span>
<span class="normal">726</span>
<span class="normal">727</span>
<span class="normal">728</span>
<span class="normal">729</span>
<span class="normal">730</span>
<span class="normal">731</span>
<span class="normal">732</span>
<span class="normal">733</span>
<span class="normal">734</span>
<span class="normal">735</span>
<span class="normal">736</span>
<span class="normal">737</span>
<span class="normal">738</span>
<span class="normal">739</span>
<span class="normal">740</span>
<span class="normal">741</span>
<span class="normal">742</span>
<span class="normal">743</span>
<span class="normal">744</span>
<span class="normal">745</span>
<span class="normal">746</span>
<span class="normal">747</span>
<span class="normal">748</span>
<span class="normal">749</span>
<span class="normal">750</span>
<span class="normal">751</span>
<span class="normal">752</span>
<span class="normal">753</span>
<span class="normal">754</span>
<span class="normal">755</span>
<span class="normal">756</span>
<span class="normal">757</span>
<span class="normal">758</span>
<span class="normal">759</span>
<span class="normal">760</span>
<span class="normal">761</span>
<span class="normal">762</span>
<span class="normal">763</span>
<span class="normal">764</span>
<span class="normal">765</span>
<span class="normal">766</span>
<span class="normal">767</span>
<span class="normal">768</span>
<span class="normal">769</span>
<span class="normal">770</span>
<span class="normal">771</span>
<span class="normal">772</span>
<span class="normal">773</span></pre></div></td><td class="code"><div><pre id="__code_34"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_34 > code"></button><code tabindex="0"><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">next</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">node</span><span class="p">:</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Manually drive the graph run by passing in the node you want to run next.</span>

<span class="sd">    This lets you inspect or mutate the node before continuing execution, or skip certain nodes</span>
<span class="sd">    under dynamic conditions. The graph run should stop when you return an [`End`][pydantic_graph.nodes.End] node.</span>

<span class="sd">    Here's an example of using `next` to drive the graph from [above][pydantic_graph.graph.Graph]:</span>
<span class="sd">    ```py {title="next_never_42.py" noqa="I001" py="3.10"}</span>
<span class="sd">    from copy import deepcopy</span>
<span class="sd">    from pydantic_graph import End</span>
<span class="sd">    from never_42 import Increment, MyState, never_42_graph</span>

<span class="sd">    async def main():</span>
<span class="sd">        state = MyState(48)</span>
<span class="sd">        async with never_42_graph.iter(Increment(), state=state) as graph_run:</span>
<span class="sd">            next_node = graph_run.next_node  # start with the first node</span>
<span class="sd">            node_states = [(next_node, deepcopy(graph_run.state))]</span>

<span class="sd">            while not isinstance(next_node, End):</span>
<span class="sd">                if graph_run.state.number == 50:</span>
<span class="sd">                    graph_run.state.number = 42</span>
<span class="sd">                next_node = await graph_run.next(next_node)</span>
<span class="sd">                node_states.append((next_node, deepcopy(graph_run.state)))</span>

<span class="sd">            print(node_states)</span>
<span class="sd">            '''</span>
<span class="sd">            [</span>
<span class="sd">                (Increment(), MyState(number=48)),</span>
<span class="sd">                (Check42(), MyState(number=49)),</span>
<span class="sd">                (End(data=49), MyState(number=49)),</span>
<span class="sd">            ]</span>
<span class="sd">            '''</span>
<span class="sd">    ```</span>

<span class="sd">    Args:</span>
<span class="sd">        node: The node to run next in the graph. If not specified, uses `self.next_node`, which is initialized to</span>
<span class="sd">            the `start_node` of the run and updated each time a new node is returned.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The next node returned by the graph logic, or an [`End`][pydantic_graph.nodes.End] node if</span>
<span class="sd">        the run has completed.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">node</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># This cast is necessary because self._next_node could be an `End`. You'll get a runtime error if that's</span>
        <span class="c1"># the case, but if it is, the only way to get there would be to have tried calling next manually after</span>
        <span class="c1"># the run finished. Either way, maybe it would be better to not do this cast...</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">)</span>
        <span class="n">node_snapshot_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_snapshot_id</span><span class="p">()</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">node_snapshot_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_snapshot_id</span><span class="p">()</span>

    <span class="k">if</span> <span class="n">node_snapshot_id</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_snapshot_id</span><span class="p">:</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">persistence</span><span class="o">.</span><span class="n">snapshot_node_if_new</span><span class="p">(</span><span class="n">node_snapshot_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_snapshot_id</span> <span class="o">=</span> <span class="n">node_snapshot_id</span>

    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">node</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">):</span>
        <span class="c1"># While technically this is not compatible with the documented method signature, it's an easy mistake to</span>
        <span class="c1"># make, and we should eagerly provide a more helpful error message than you'd get otherwise.</span>
        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'`next` must be called with a `BaseNode` instance, got </span><span class="si">{</span><span class="n">node</span><span class="si">!r}</span><span class="s1">.'</span><span class="p">)</span>

    <span class="n">node_id</span> <span class="o">=</span> <span class="n">node</span><span class="o">.</span><span class="n">get_node_id</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">node_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph</span><span class="o">.</span><span class="n">node_defs</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">GraphRuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Node `</span><span class="si">{</span><span class="n">node</span><span class="si">}</span><span class="s1">` is not in the graph.'</span><span class="p">)</span>

    <span class="k">with</span> <span class="n">ExitStack</span><span class="p">()</span> <span class="k">as</span> <span class="n">stack</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph</span><span class="o">.</span><span class="n">auto_instrument</span><span class="p">:</span>
            <span class="n">stack</span><span class="o">.</span><span class="n">enter_context</span><span class="p">(</span><span class="n">_logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'run node </span><span class="si">{node_id}</span><span class="s1">'</span><span class="p">,</span> <span class="n">node_id</span><span class="o">=</span><span class="n">node_id</span><span class="p">,</span> <span class="n">node</span><span class="o">=</span><span class="n">node</span><span class="p">))</span>

        <span class="k">async</span> <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">persistence</span><span class="o">.</span><span class="n">record_run</span><span class="p">(</span><span class="n">node_snapshot_id</span><span class="p">):</span>
            <span class="n">ctx</span> <span class="o">=</span> <span class="n">GraphRunContext</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">deps</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span> <span class="o">=</span> <span class="k">await</span> <span class="n">node</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>

    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">,</span> <span class="n">End</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_snapshot_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="o">.</span><span class="n">get_snapshot_id</span><span class="p">()</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">persistence</span><span class="o">.</span><span class="n">snapshot_end</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">)</span>
    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">,</span> <span class="n">BaseNode</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_snapshot_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="o">.</span><span class="n">get_snapshot_id</span><span class="p">()</span>
        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">persistence</span><span class="o">.</span><span class="n">snapshot_node</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">exceptions</span><span class="o">.</span><span class="n">GraphRuntimeError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s1">'Invalid node return type: `</span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">`. Expected `BaseNode` or `End`.'</span>
        <span class="p">)</span>

    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_graph.graph.GraphRun.__anext__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__anext__</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_35"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_35 > code"></button><code><span class="fm">__anext__</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">(</span>
    <span class="nf"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.BaseNode" href="../nodes/#pydantic_graph.nodes.BaseNode">BaseNode</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.DepsT" href="../nodes/#pydantic_graph.nodes.DepsT">DepsT</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.End" href="../nodes/#pydantic_graph.nodes.End">End</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a></span><span class="p">]</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Use the last returned node as the input to <code>Graph.next</code>.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">778</span>
<span class="normal">779</span>
<span class="normal">780</span>
<span class="normal">781</span>
<span class="normal">782</span></pre></div></td><td class="code"><div><pre id="__code_36"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_36 > code"></button><code><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="fm">__anext__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseNode</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">DepsT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">|</span> <span class="n">End</span><span class="p">[</span><span class="n">RunEndT</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Use the last returned node as the input to `Graph.next`."""</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">,</span> <span class="n">End</span><span class="p">):</span>
        <span class="k">raise</span> <span class="ne">StopAsyncIteration</span>
    <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">next</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_next_node</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_graph.graph.GraphRunResult" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">GraphRunResult</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.nodes.StateT" href="../nodes/#pydantic_graph.nodes.StateT">StateT</a>, <a class="autorefs autorefs-internal" title="pydantic_graph.nodes.RunEndT" href="../nodes/#pydantic_graph.nodes.RunEndT">RunEndT</a>]</code></p>


        <p>The final result of running a graph.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_graph/pydantic_graph/graph.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">788</span>
<span class="normal">789</span>
<span class="normal">790</span>
<span class="normal">791</span>
<span class="normal">792</span>
<span class="normal">793</span>
<span class="normal">794</span></pre></div></td><td class="code"><div><pre id="__code_37"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_37 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">GraphRunResult</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""The final result of running a graph."""</span>

    <span class="n">output</span><span class="p">:</span> <span class="n">RunEndT</span>
    <span class="n">state</span><span class="p">:</span> <span class="n">StateT</span>
    <span class="n">persistence</span><span class="p">:</span> <span class="n">BaseStatePersistence</span><span class="p">[</span><span class="n">StateT</span><span class="p">,</span> <span class="n">RunEndT</span><span class="p">]</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





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
    
    
    <script id="__config" type="application/json">{"base": "../../..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../../../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../../../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>