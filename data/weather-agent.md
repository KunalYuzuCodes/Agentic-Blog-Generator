<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/examples/weather-agent/">
      
      
        <link rel="prev" href="../pydantic-model/">
      
      
        <link rel="next" href="../bank-support/">
      
      
      <link rel="icon" href="../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>Weather agent - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="Weather agent - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/examples/weather-agent.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/examples/weather-agent/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="Weather agent - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/examples/weather-agent.png">
      
    
    
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
      
        
        <a href="#running-the-example" class="md-skip">
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
            
              Weather agent
            
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
  

    
      
      
  
  
    
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7" checked="">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_7" id="__nav_7_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            Examples
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#running-the-example" class="md-nav__link">
    <span class="md-ellipsis">
      Running the Example
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#example-code" class="md-nav__link">
    <span class="md-ellipsis">
      Example Code
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#running-the-ui" class="md-nav__link">
    <span class="md-ellipsis">
      Running the UI
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#ui-code" class="md-nav__link">
    <span class="md-ellipsis">
      UI Code
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../api/pydantic_evals/generation/" class="md-nav__link">
        
  
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
  <a href="#running-the-example" class="md-nav__link">
    <span class="md-ellipsis">
      Running the Example
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#example-code" class="md-nav__link">
    <span class="md-ellipsis">
      Example Code
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#running-the-ui" class="md-nav__link">
    <span class="md-ellipsis">
      Running the UI
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#ui-code" class="md-nav__link">
    <span class="md-ellipsis">
      UI Code
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
                
                  


  
  


  <h1>Weather agent</h1>

<p>Example of PydanticAI with multiple tools which the LLM needs to call in turn to answer a question.</p>
<p>Demonstrates:</p>
<ul>
<li><a href="../../tools/">tools</a></li>
<li><a href="../../dependencies/">agent dependencies</a></li>
<li><a href="../../results/#streaming-text">streaming text responses</a></li>
<li>Building a <a href="https://www.gradio.app/">Gradio</a> UI for the agent</li>
</ul>
<p>In this case the idea is a "weather" agent — the user can ask for the weather in multiple locations,
the agent will use the <code>get_lat_lng</code> tool to get the latitude and longitude of the locations, then use
the <code>get_weather</code> tool to get the weather for those locations.</p>
<h2 id="running-the-example">Running the Example</h2>
<p>To run this example properly, you might want to add two extra API keys <strong>(Note if either key is missing, the code will fall back to dummy data, so they're not required)</strong>:</p>
<ul>
<li>A weather API key from <a href="https://www.tomorrow.io/weather-api/">tomorrow.io</a> set via <code>WEATHER_API_KEY</code></li>
<li>A geocoding API key from <a href="https://geocode.maps.co/">geocode.maps.co</a> set via <code>GEO_API_KEY</code></li>
</ul>
<p>With <a href="../#usage">dependencies installed and environment variables set</a>, run:</p>
<div class="tabbed-set tabbed-alternate" data-tabs="1:2" style="--md-indicator-x: 0px; --md-indicator-width: 50px;"><input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio"><input id="__tabbed_1_2" name="__tabbed_1" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_1_1"><a href="#__tabbed_1_1" tabindex="-1">pip</a></label><label for="__tabbed_1_2"><a href="#__tabbed_1_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code>python<span class="w"> </span>-m<span class="w"> </span>pydantic_ai_examples.weather_agent
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code>uv<span class="w"> </span>run<span class="w"> </span>-m<span class="w"> </span>pydantic_ai_examples.weather_agent
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<h2 id="example-code">Example Code</h2>
<div class="language-python highlight"><span class="filename">pydantic_ai_examples/weather_agent.py</span><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">__future__</span><span class="w"> </span><span class="kn">import</span> <span class="n">annotations</span> <span class="k">as</span> <span class="n">_annotations</span>

<span class="kn">import</span><span class="w"> </span><span class="nn">asyncio</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">os</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">dataclasses</span><span class="w"> </span><span class="kn">import</span> <span class="n">dataclass</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">typing</span><span class="w"> </span><span class="kn">import</span> <span class="n">Any</span>

<span class="kn">import</span><span class="w"> </span><span class="nn">logfire</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">devtools</span><span class="w"> </span><span class="kn">import</span> <span class="n">debug</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">httpx</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncClient</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">ModelRetry</span><span class="p">,</span> <span class="n">RunContext</span>

<span class="c1"># 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured</span>
<span class="n">logfire</span><span class="o">.</span><span class="n">configure</span><span class="p">(</span><span class="n">send_to_logfire</span><span class="o">=</span><span class="s1">'if-token-present'</span><span class="p">)</span>


<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Deps</span><span class="p">:</span>
    <span class="n">client</span><span class="p">:</span> <span class="n">AsyncClient</span>
    <span class="n">weather_api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">geo_api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span>


<span class="n">weather_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
    <span class="s1">'openai:gpt-4o'</span><span class="p">,</span>
    <span class="c1"># 'Be concise, reply with one sentence.' is enough for some models (like openai) to use</span>
    <span class="c1"># the below tools appropriately, but others like anthropic and gemini require a bit more direction.</span>
    <span class="n">system_prompt</span><span class="o">=</span><span class="p">(</span>
        <span class="s1">'Be concise, reply with one sentence.'</span>
        <span class="s1">'Use the `get_lat_lng` tool to get the latitude and longitude of the locations, '</span>
        <span class="s1">'then use the `get_weather` tool to get the weather.'</span>
    <span class="p">),</span>
    <span class="n">deps_type</span><span class="o">=</span><span class="n">Deps</span><span class="p">,</span>
    <span class="n">retries</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">instrument</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
<span class="p">)</span>


<span class="nd">@weather_agent</span><span class="o">.</span><span class="n">tool</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">get_lat_lng</span><span class="p">(</span>
    <span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">Deps</span><span class="p">],</span> <span class="n">location_description</span><span class="p">:</span> <span class="nb">str</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">float</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get the latitude and longitude of a location.</span>

<span class="sd">    Args:</span>
<span class="sd">        ctx: The context.</span>
<span class="sd">        location_description: A description of a location.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">geo_api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># if no API key is provided, return a dummy response (London)</span>
        <span class="k">return</span> <span class="p">{</span><span class="s1">'lat'</span><span class="p">:</span> <span class="mf">51.1</span><span class="p">,</span> <span class="s1">'lng'</span><span class="p">:</span> <span class="o">-</span><span class="mf">0.1</span><span class="p">}</span>

    <span class="n">params</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s1">'q'</span><span class="p">:</span> <span class="n">location_description</span><span class="p">,</span>
        <span class="s1">'api_key'</span><span class="p">:</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">geo_api_key</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="k">with</span> <span class="n">logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'calling geocode API'</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">)</span> <span class="k">as</span> <span class="n">span</span><span class="p">:</span>
        <span class="n">r</span> <span class="o">=</span> <span class="k">await</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'https://geocode.maps.co/search'</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>
        <span class="n">r</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">r</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="n">span</span><span class="o">.</span><span class="n">set_attribute</span><span class="p">(</span><span class="s1">'response'</span><span class="p">,</span> <span class="n">data</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">data</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">{</span><span class="s1">'lat'</span><span class="p">:</span> <span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s1">'lat'</span><span class="p">],</span> <span class="s1">'lng'</span><span class="p">:</span> <span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s1">'lon'</span><span class="p">]}</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">ModelRetry</span><span class="p">(</span><span class="s1">'Could not find the location'</span><span class="p">)</span>


<span class="nd">@weather_agent</span><span class="o">.</span><span class="n">tool</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">get_weather</span><span class="p">(</span><span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">Deps</span><span class="p">],</span> <span class="n">lat</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">lng</span><span class="p">:</span> <span class="nb">float</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Get the weather at a location.</span>

<span class="sd">    Args:</span>
<span class="sd">        ctx: The context.</span>
<span class="sd">        lat: Latitude of the location.</span>
<span class="sd">        lng: Longitude of the location.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">weather_api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="c1"># if no API key is provided, return a dummy response</span>
        <span class="k">return</span> <span class="p">{</span><span class="s1">'temperature'</span><span class="p">:</span> <span class="s1">'21 °C'</span><span class="p">,</span> <span class="s1">'description'</span><span class="p">:</span> <span class="s1">'Sunny'</span><span class="p">}</span>

    <span class="n">params</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s1">'apikey'</span><span class="p">:</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">weather_api_key</span><span class="p">,</span>
        <span class="s1">'location'</span><span class="p">:</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">lat</span><span class="si">}</span><span class="s1">,</span><span class="si">{</span><span class="n">lng</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span>
        <span class="s1">'units'</span><span class="p">:</span> <span class="s1">'metric'</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="k">with</span> <span class="n">logfire</span><span class="o">.</span><span class="n">span</span><span class="p">(</span><span class="s1">'calling weather API'</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">)</span> <span class="k">as</span> <span class="n">span</span><span class="p">:</span>
        <span class="n">r</span> <span class="o">=</span> <span class="k">await</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">get</span><span class="p">(</span>
            <span class="s1">'https://api.tomorrow.io/v4/weather/realtime'</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">params</span>
        <span class="p">)</span>
        <span class="n">r</span><span class="o">.</span><span class="n">raise_for_status</span><span class="p">()</span>
        <span class="n">data</span> <span class="o">=</span> <span class="n">r</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
        <span class="n">span</span><span class="o">.</span><span class="n">set_attribute</span><span class="p">(</span><span class="s1">'response'</span><span class="p">,</span> <span class="n">data</span><span class="p">)</span>

    <span class="n">values</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s1">'data'</span><span class="p">][</span><span class="s1">'values'</span><span class="p">]</span>
    <span class="c1"># https://docs.tomorrow.io/reference/data-layers-weather-codes</span>
    <span class="n">code_lookup</span> <span class="o">=</span> <span class="p">{</span>
        <span class="mi">1000</span><span class="p">:</span> <span class="s1">'Clear, Sunny'</span><span class="p">,</span>
        <span class="mi">1100</span><span class="p">:</span> <span class="s1">'Mostly Clear'</span><span class="p">,</span>
        <span class="mi">1101</span><span class="p">:</span> <span class="s1">'Partly Cloudy'</span><span class="p">,</span>
        <span class="mi">1102</span><span class="p">:</span> <span class="s1">'Mostly Cloudy'</span><span class="p">,</span>
        <span class="mi">1001</span><span class="p">:</span> <span class="s1">'Cloudy'</span><span class="p">,</span>
        <span class="mi">2000</span><span class="p">:</span> <span class="s1">'Fog'</span><span class="p">,</span>
        <span class="mi">2100</span><span class="p">:</span> <span class="s1">'Light Fog'</span><span class="p">,</span>
        <span class="mi">4000</span><span class="p">:</span> <span class="s1">'Drizzle'</span><span class="p">,</span>
        <span class="mi">4001</span><span class="p">:</span> <span class="s1">'Rain'</span><span class="p">,</span>
        <span class="mi">4200</span><span class="p">:</span> <span class="s1">'Light Rain'</span><span class="p">,</span>
        <span class="mi">4201</span><span class="p">:</span> <span class="s1">'Heavy Rain'</span><span class="p">,</span>
        <span class="mi">5000</span><span class="p">:</span> <span class="s1">'Snow'</span><span class="p">,</span>
        <span class="mi">5001</span><span class="p">:</span> <span class="s1">'Flurries'</span><span class="p">,</span>
        <span class="mi">5100</span><span class="p">:</span> <span class="s1">'Light Snow'</span><span class="p">,</span>
        <span class="mi">5101</span><span class="p">:</span> <span class="s1">'Heavy Snow'</span><span class="p">,</span>
        <span class="mi">6000</span><span class="p">:</span> <span class="s1">'Freezing Drizzle'</span><span class="p">,</span>
        <span class="mi">6001</span><span class="p">:</span> <span class="s1">'Freezing Rain'</span><span class="p">,</span>
        <span class="mi">6200</span><span class="p">:</span> <span class="s1">'Light Freezing Rain'</span><span class="p">,</span>
        <span class="mi">6201</span><span class="p">:</span> <span class="s1">'Heavy Freezing Rain'</span><span class="p">,</span>
        <span class="mi">7000</span><span class="p">:</span> <span class="s1">'Ice Pellets'</span><span class="p">,</span>
        <span class="mi">7101</span><span class="p">:</span> <span class="s1">'Heavy Ice Pellets'</span><span class="p">,</span>
        <span class="mi">7102</span><span class="p">:</span> <span class="s1">'Light Ice Pellets'</span><span class="p">,</span>
        <span class="mi">8000</span><span class="p">:</span> <span class="s1">'Thunderstorm'</span><span class="p">,</span>
    <span class="p">}</span>
    <span class="k">return</span> <span class="p">{</span>
        <span class="s1">'temperature'</span><span class="p">:</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">values</span><span class="p">[</span><span class="s2">"temperatureApparent"</span><span class="p">]</span><span class="si">:</span><span class="s1">0.0f</span><span class="si">}</span><span class="s1">°C'</span><span class="p">,</span>
        <span class="s1">'description'</span><span class="p">:</span> <span class="n">code_lookup</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">values</span><span class="p">[</span><span class="s1">'weatherCode'</span><span class="p">],</span> <span class="s1">'Unknown'</span><span class="p">),</span>
    <span class="p">}</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">main</span><span class="p">():</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">AsyncClient</span><span class="p">()</span> <span class="k">as</span> <span class="n">client</span><span class="p">:</span>
        <span class="c1"># create a free API key at https://www.tomorrow.io/weather-api/</span>
        <span class="n">weather_api_key</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s1">'WEATHER_API_KEY'</span><span class="p">)</span>
        <span class="c1"># create a free API key at https://geocode.maps.co/</span>
        <span class="n">geo_api_key</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s1">'GEO_API_KEY'</span><span class="p">)</span>
        <span class="n">deps</span> <span class="o">=</span> <span class="n">Deps</span><span class="p">(</span>
            <span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span> <span class="n">weather_api_key</span><span class="o">=</span><span class="n">weather_api_key</span><span class="p">,</span> <span class="n">geo_api_key</span><span class="o">=</span><span class="n">geo_api_key</span>
        <span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">weather_agent</span><span class="o">.</span><span class="n">run</span><span class="p">(</span>
            <span class="s1">'What is the weather like in London and in Wiltshire?'</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">deps</span>
        <span class="p">)</span>
        <span class="n">debug</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s1">'Response:'</span><span class="p">,</span> <span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>


<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s1">'__main__'</span><span class="p">:</span>
    <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">main</span><span class="p">())</span>
</code></pre></div>
<h2 id="running-the-ui">Running the UI</h2>
<p>You can build multi-turn chat applications for your agent with <a href="https://www.gradio.app/">Gradio</a>, a framework for building AI web applications entirely in python. Gradio comes with built-in chat components and agent support so the entire UI will be implemented in a single python file!</p>
<p>Here's what the UI looks like for the weather agent:</p>
<div style="position: relative; padding-top: 67%;">
  <iframe src="https://customer-nmegqx24430okhaq.cloudflarestream.com/c549d8d8827ded15f326f998e428e6c3/iframe?poster=https%3A%2F%2Fcustomer-nmegqx24430okhaq.cloudflarestream.com%2Fc549d8d8827ded15f326f998e428e6c3%2Fthumbnails%2Fthumbnail.jpg%3Ftime%3D6s%26height%3D600" loading="lazy" style="border: none; position: absolute; top: 0; left: 0; height: 100%; width: 100%;" allow="accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;" allowfullscreen="true"></iframe>
</div>

<p>Note, to run the UI, you'll need Python 3.10+.</p>
<div class="language-bash highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code>pip<span class="w"> </span>install<span class="w"> </span>gradio&gt;<span class="o">=</span><span class="m">5</span>.9.0
python/uv-run<span class="w"> </span>-m<span class="w"> </span>pydantic_ai_examples.weather_agent_gradio
</code></pre></div>
<h2 id="ui-code">UI Code</h2>
<div class="language-python highlight"><span class="filename">pydantic_ai_examples/weather_agent_gradio.py</span><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">__future__</span><span class="w"> </span><span class="kn">import</span> <span class="n">annotations</span> <span class="k">as</span> <span class="n">_annotations</span>

<span class="kn">import</span><span class="w"> </span><span class="nn">json</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">os</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">httpx</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncClient</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.messages</span><span class="w"> </span><span class="kn">import</span> <span class="n">ToolCallPart</span><span class="p">,</span> <span class="n">ToolReturnPart</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai_examples.weather_agent</span><span class="w"> </span><span class="kn">import</span> <span class="n">Deps</span><span class="p">,</span> <span class="n">weather_agent</span>

<span class="k">try</span><span class="p">:</span>
    <span class="kn">import</span><span class="w"> </span><span class="nn">gradio</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">gr</span>
<span class="k">except</span> <span class="ne">ImportError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
    <span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span>
        <span class="s1">'Please install gradio with `pip install gradio`. You must use python&gt;=3.10.'</span>
    <span class="p">)</span> <span class="kn">from</span><span class="w"> </span><span class="nn">e</span>

<span class="n">TOOL_TO_DISPLAY_NAME</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'get_lat_lng'</span><span class="p">:</span> <span class="s1">'Geocoding API'</span><span class="p">,</span> <span class="s1">'get_weather'</span><span class="p">:</span> <span class="s1">'Weather API'</span><span class="p">}</span>

<span class="n">client</span> <span class="o">=</span> <span class="n">AsyncClient</span><span class="p">()</span>
<span class="n">weather_api_key</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s1">'WEATHER_API_KEY'</span><span class="p">)</span>
<span class="c1"># create a free API key at https://geocode.maps.co/</span>
<span class="n">geo_api_key</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s1">'GEO_API_KEY'</span><span class="p">)</span>
<span class="n">deps</span> <span class="o">=</span> <span class="n">Deps</span><span class="p">(</span><span class="n">client</span><span class="o">=</span><span class="n">client</span><span class="p">,</span> <span class="n">weather_api_key</span><span class="o">=</span><span class="n">weather_api_key</span><span class="p">,</span> <span class="n">geo_api_key</span><span class="o">=</span><span class="n">geo_api_key</span><span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">stream_from_agent</span><span class="p">(</span><span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">chatbot</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">dict</span><span class="p">],</span> <span class="n">past_messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">):</span>
    <span class="n">chatbot</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="s1">'role'</span><span class="p">:</span> <span class="s1">'user'</span><span class="p">,</span> <span class="s1">'content'</span><span class="p">:</span> <span class="n">prompt</span><span class="p">})</span>
    <span class="k">yield</span> <span class="n">gr</span><span class="o">.</span><span class="n">Textbox</span><span class="p">(</span><span class="n">interactive</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="s1">''</span><span class="p">),</span> <span class="n">chatbot</span><span class="p">,</span> <span class="n">gr</span><span class="o">.</span><span class="n">skip</span><span class="p">()</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">weather_agent</span><span class="o">.</span><span class="n">run_stream</span><span class="p">(</span>
        <span class="n">prompt</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">deps</span><span class="p">,</span> <span class="n">message_history</span><span class="o">=</span><span class="n">past_messages</span>
    <span class="p">)</span> <span class="k">as</span> <span class="n">result</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">result</span><span class="o">.</span><span class="n">new_messages</span><span class="p">():</span>
            <span class="k">for</span> <span class="n">call</span> <span class="ow">in</span> <span class="n">message</span><span class="o">.</span><span class="n">parts</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">call</span><span class="p">,</span> <span class="n">ToolCallPart</span><span class="p">):</span>
                    <span class="n">call_args</span> <span class="o">=</span> <span class="p">(</span>
                        <span class="n">call</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">args_json</span>
                        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">call</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="s1">'args_json'</span><span class="p">)</span>
                        <span class="k">else</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">call</span><span class="o">.</span><span class="n">args</span><span class="o">.</span><span class="n">args_dict</span><span class="p">)</span>
                    <span class="p">)</span>
                    <span class="n">metadata</span> <span class="o">=</span> <span class="p">{</span>
                        <span class="s1">'title'</span><span class="p">:</span> <span class="sa">f</span><span class="s1">'🛠️ Using </span><span class="si">{</span><span class="n">TOOL_TO_DISPLAY_NAME</span><span class="p">[</span><span class="n">call</span><span class="o">.</span><span class="n">tool_name</span><span class="p">]</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span>
                    <span class="p">}</span>
                    <span class="k">if</span> <span class="n">call</span><span class="o">.</span><span class="n">tool_call_id</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                        <span class="n">metadata</span><span class="p">[</span><span class="s1">'id'</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">call</span><span class="o">.</span><span class="n">tool_call_id</span><span class="p">}</span>

                    <span class="n">gr_message</span> <span class="o">=</span> <span class="p">{</span>
                        <span class="s1">'role'</span><span class="p">:</span> <span class="s1">'assistant'</span><span class="p">,</span>
                        <span class="s1">'content'</span><span class="p">:</span> <span class="s1">'Parameters: '</span> <span class="o">+</span> <span class="n">call_args</span><span class="p">,</span>
                        <span class="s1">'metadata'</span><span class="p">:</span> <span class="n">metadata</span><span class="p">,</span>
                    <span class="p">}</span>
                    <span class="n">chatbot</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">gr_message</span><span class="p">)</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">call</span><span class="p">,</span> <span class="n">ToolReturnPart</span><span class="p">):</span>
                    <span class="k">for</span> <span class="n">gr_message</span> <span class="ow">in</span> <span class="n">chatbot</span><span class="p">:</span>
                        <span class="k">if</span> <span class="p">(</span>
                            <span class="n">gr_message</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'metadata'</span><span class="p">,</span> <span class="p">{})</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'id'</span><span class="p">,</span> <span class="s1">''</span><span class="p">)</span>
                            <span class="o">==</span> <span class="n">call</span><span class="o">.</span><span class="n">tool_call_id</span>
                        <span class="p">):</span>
                            <span class="n">gr_message</span><span class="p">[</span><span class="s1">'content'</span><span class="p">]</span> <span class="o">+=</span> <span class="p">(</span>
                                <span class="sa">f</span><span class="s1">'</span><span class="se">\n</span><span class="s1">Output: </span><span class="si">{</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">call</span><span class="o">.</span><span class="n">content</span><span class="p">)</span><span class="si">}</span><span class="s1">'</span>
                            <span class="p">)</span>
                <span class="k">yield</span> <span class="n">gr</span><span class="o">.</span><span class="n">skip</span><span class="p">(),</span> <span class="n">chatbot</span><span class="p">,</span> <span class="n">gr</span><span class="o">.</span><span class="n">skip</span><span class="p">()</span>
        <span class="n">chatbot</span><span class="o">.</span><span class="n">append</span><span class="p">({</span><span class="s1">'role'</span><span class="p">:</span> <span class="s1">'assistant'</span><span class="p">,</span> <span class="s1">'content'</span><span class="p">:</span> <span class="s1">''</span><span class="p">})</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">message</span> <span class="ow">in</span> <span class="n">result</span><span class="o">.</span><span class="n">stream_text</span><span class="p">():</span>
            <span class="n">chatbot</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">][</span><span class="s1">'content'</span><span class="p">]</span> <span class="o">=</span> <span class="n">message</span>
            <span class="k">yield</span> <span class="n">gr</span><span class="o">.</span><span class="n">skip</span><span class="p">(),</span> <span class="n">chatbot</span><span class="p">,</span> <span class="n">gr</span><span class="o">.</span><span class="n">skip</span><span class="p">()</span>
        <span class="n">past_messages</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">all_messages</span><span class="p">()</span>

        <span class="k">yield</span> <span class="n">gr</span><span class="o">.</span><span class="n">Textbox</span><span class="p">(</span><span class="n">interactive</span><span class="o">=</span><span class="kc">True</span><span class="p">),</span> <span class="n">gr</span><span class="o">.</span><span class="n">skip</span><span class="p">(),</span> <span class="n">past_messages</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">handle_retry</span><span class="p">(</span><span class="n">chatbot</span><span class="p">,</span> <span class="n">past_messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">,</span> <span class="n">retry_data</span><span class="p">:</span> <span class="n">gr</span><span class="o">.</span><span class="n">RetryData</span><span class="p">):</span>
    <span class="n">new_history</span> <span class="o">=</span> <span class="n">chatbot</span><span class="p">[:</span> <span class="n">retry_data</span><span class="o">.</span><span class="n">index</span><span class="p">]</span>
    <span class="n">previous_prompt</span> <span class="o">=</span> <span class="n">chatbot</span><span class="p">[</span><span class="n">retry_data</span><span class="o">.</span><span class="n">index</span><span class="p">][</span><span class="s1">'content'</span><span class="p">]</span>
    <span class="n">past_messages</span> <span class="o">=</span> <span class="n">past_messages</span><span class="p">[:</span> <span class="n">retry_data</span><span class="o">.</span><span class="n">index</span><span class="p">]</span>
    <span class="k">async</span> <span class="k">for</span> <span class="n">update</span> <span class="ow">in</span> <span class="n">stream_from_agent</span><span class="p">(</span><span class="n">previous_prompt</span><span class="p">,</span> <span class="n">new_history</span><span class="p">,</span> <span class="n">past_messages</span><span class="p">):</span>
        <span class="k">yield</span> <span class="n">update</span>


<span class="k">def</span><span class="w"> </span><span class="nf">undo</span><span class="p">(</span><span class="n">chatbot</span><span class="p">,</span> <span class="n">past_messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">,</span> <span class="n">undo_data</span><span class="p">:</span> <span class="n">gr</span><span class="o">.</span><span class="n">UndoData</span><span class="p">):</span>
    <span class="n">new_history</span> <span class="o">=</span> <span class="n">chatbot</span><span class="p">[:</span> <span class="n">undo_data</span><span class="o">.</span><span class="n">index</span><span class="p">]</span>
    <span class="n">past_messages</span> <span class="o">=</span> <span class="n">past_messages</span><span class="p">[:</span> <span class="n">undo_data</span><span class="o">.</span><span class="n">index</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">chatbot</span><span class="p">[</span><span class="n">undo_data</span><span class="o">.</span><span class="n">index</span><span class="p">][</span><span class="s1">'content'</span><span class="p">],</span> <span class="n">new_history</span><span class="p">,</span> <span class="n">past_messages</span>


<span class="k">def</span><span class="w"> </span><span class="nf">select_data</span><span class="p">(</span><span class="n">message</span><span class="p">:</span> <span class="n">gr</span><span class="o">.</span><span class="n">SelectData</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">return</span> <span class="n">message</span><span class="o">.</span><span class="n">value</span><span class="p">[</span><span class="s1">'text'</span><span class="p">]</span>


<span class="k">with</span> <span class="n">gr</span><span class="o">.</span><span class="n">Blocks</span><span class="p">()</span> <span class="k">as</span> <span class="n">demo</span><span class="p">:</span>
    <span class="n">gr</span><span class="o">.</span><span class="n">HTML</span><span class="p">(</span>
<span class="w">        </span><span class="sd">"""</span>
<span class="sd">&lt;div style="display: flex; justify-content: center; align-items: center; gap: 2rem; padding: 1rem; width: 100%"&gt;</span>
<span class="sd">    &lt;img src="https://ai.pydantic.dev/img/logo-white.svg" style="max-width: 200px; height: auto"&gt;</span>
<span class="sd">    &lt;div&gt;</span>
<span class="sd">        &lt;h1 style="margin: 0 0 1rem 0"&gt;Weather Assistant&lt;/h1&gt;</span>
<span class="sd">        &lt;h3 style="margin: 0 0 0.5rem 0"&gt;</span>
<span class="sd">            This assistant answer your weather questions.</span>
<span class="sd">        &lt;/h3&gt;</span>
<span class="sd">    &lt;/div&gt;</span>
<span class="sd">&lt;/div&gt;</span>
<span class="sd">"""</span>
    <span class="p">)</span>
    <span class="n">past_messages</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">State</span><span class="p">([])</span>
    <span class="n">chatbot</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">Chatbot</span><span class="p">(</span>
        <span class="n">label</span><span class="o">=</span><span class="s1">'Packing Assistant'</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s1">'messages'</span><span class="p">,</span>
        <span class="n">avatar_images</span><span class="o">=</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="s1">'https://ai.pydantic.dev/img/logo-white.svg'</span><span class="p">),</span>
        <span class="n">examples</span><span class="o">=</span><span class="p">[</span>
            <span class="p">{</span><span class="s1">'text'</span><span class="p">:</span> <span class="s1">'What is the weather like in Miami?'</span><span class="p">},</span>
            <span class="p">{</span><span class="s1">'text'</span><span class="p">:</span> <span class="s1">'What is the weather like in London?'</span><span class="p">},</span>
        <span class="p">],</span>
    <span class="p">)</span>
    <span class="k">with</span> <span class="n">gr</span><span class="o">.</span><span class="n">Row</span><span class="p">():</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="n">gr</span><span class="o">.</span><span class="n">Textbox</span><span class="p">(</span>
            <span class="n">lines</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="n">show_label</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">placeholder</span><span class="o">=</span><span class="s1">'What is the weather like in New York City?'</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="n">generation</span> <span class="o">=</span> <span class="n">prompt</span><span class="o">.</span><span class="n">submit</span><span class="p">(</span>
        <span class="n">stream_from_agent</span><span class="p">,</span>
        <span class="n">inputs</span><span class="o">=</span><span class="p">[</span><span class="n">prompt</span><span class="p">,</span> <span class="n">chatbot</span><span class="p">,</span> <span class="n">past_messages</span><span class="p">],</span>
        <span class="n">outputs</span><span class="o">=</span><span class="p">[</span><span class="n">prompt</span><span class="p">,</span> <span class="n">chatbot</span><span class="p">,</span> <span class="n">past_messages</span><span class="p">],</span>
    <span class="p">)</span>
    <span class="n">chatbot</span><span class="o">.</span><span class="n">example_select</span><span class="p">(</span><span class="n">select_data</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="p">[</span><span class="n">prompt</span><span class="p">])</span>
    <span class="n">chatbot</span><span class="o">.</span><span class="n">retry</span><span class="p">(</span>
        <span class="n">handle_retry</span><span class="p">,</span> <span class="p">[</span><span class="n">chatbot</span><span class="p">,</span> <span class="n">past_messages</span><span class="p">],</span> <span class="p">[</span><span class="n">prompt</span><span class="p">,</span> <span class="n">chatbot</span><span class="p">,</span> <span class="n">past_messages</span><span class="p">]</span>
    <span class="p">)</span>
    <span class="n">chatbot</span><span class="o">.</span><span class="n">undo</span><span class="p">(</span><span class="n">undo</span><span class="p">,</span> <span class="p">[</span><span class="n">chatbot</span><span class="p">,</span> <span class="n">past_messages</span><span class="p">],</span> <span class="p">[</span><span class="n">prompt</span><span class="p">,</span> <span class="n">chatbot</span><span class="p">,</span> <span class="n">past_messages</span><span class="p">])</span>


<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s1">'__main__'</span><span class="p">:</span>
    <span class="n">demo</span><span class="o">.</span><span class="n">launch</span><span class="p">()</span>
</code></pre></div>







  
  






                
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